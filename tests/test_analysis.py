import os
import subprocess
from bs4 import BeautifulSoup


def test_jee_example_app_analysis(analysis_data):
    windup_path = os.getenv('WINDUP_CLI_PATH')
    report_path = os.getenv('REPORT_OUTPUT_PATH')
    application_data = analysis_data['jee_example_app']
    binary_path = os.path.join(
        os.getenv('PROJECT_PATH'),
        "fixtures/applications",
        application_data['file_name']
    )
    source = application_data['source']

    command = windup_path + ' --output ' + report_path + ' --source ' + source + ' --input ' + \
                            binary_path + ' --target ' + application_data['target'] + ' --overwrite -b '

    output = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, encoding='utf-8').stdout

    assert 'Report created' in output

    with open(report_path + "/index.html") as file:
        html_report = file.read()
    parsed_report = BeautifulSoup(html_report, 'html.parser')

    story_points = int(parsed_report.find('span', class_='points').text)

    assert story_points == application_data['story_points']
