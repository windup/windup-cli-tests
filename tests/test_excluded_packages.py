import os
import subprocess

from common.report_common import assert_story_points_from_report_file


def test_excluded_packages(analysis_data):
    application_data = analysis_data['jee_example_app']

    windup_path = os.getenv('WINDUP_CLI_PATH')
    report_path = os.getenv('REPORT_OUTPUT_PATH')
    binary_path = os.path.join(
        os.getenv('PROJECT_PATH'),
        "fixtures/applications",
        application_data['file_name']
    )

    command = windup_path + ' --output ' + report_path + ' --input ' + binary_path + ' --target ' + \
              application_data['target'] + ' --overwrite -b --source ' + application_data['source'] + \
              ' --excludePackages com.acme.anvil.service.jms'

    output = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, encoding='utf-8').stdout

    assert 'Report created' in output

    assert_story_points_from_report_file(76)

    with open(report_path + "/reports/ApplicationDetails_JEE_Example_App.html") as file:
        report_detail = file.read()

    assert 'com.acme.anvil.service.jms' not in report_detail
