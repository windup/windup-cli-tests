import os
import subprocess

from utils.command import build_command
from utils.report import assert_story_points_from_report_file


def test_excluded_packages(analysis_data):
    application_data = analysis_data['jee_example_app']

    report_path = os.getenv('REPORT_OUTPUT_PATH')

    command = build_command(
        application_data['file_name'],
        application_data['source'],
        application_data['target'],
        **{'excludePackages': 'com.acme.anvil.service.jms'}
    )

    output = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, encoding='utf-8').stdout

    assert 'Report created' in output

    assert_story_points_from_report_file(76)

    with open(report_path + '/reports/ApplicationDetails_JEE_Example_App.html') as file:
        report_detail = file.read()

    assert 'com.acme.anvil.service.jms' not in report_detail
