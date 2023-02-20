import json
import os
import subprocess

import pytest
from bs4 import BeautifulSoup


@pytest.mark.parametrize('app_name', json.load(open("data/analysis.json")))
def test_standard_analysis(app_name, analysis_data):
    application_data = analysis_data[app_name]

    windup_path = os.getenv('WINDUP_CLI_PATH')
    report_path = os.getenv('REPORT_OUTPUT_PATH')
    binary_path = os.path.join(
        os.getenv('PROJECT_PATH'),
        "fixtures/applications",
        application_data['file_name']
    )

    command = windup_path + ' --output ' + report_path + ' --input ' + binary_path + ' --target ' + \
              application_data['target'] + ' --overwrite -b '

    source = application_data['source']
    if source:
        command += ' --source ' + source

    print(command)
    output = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, encoding='utf-8').stdout

    assert 'Report created' in output

    with open(report_path + "/index.html") as file:
        html_report = file.read()
    parsed_report = BeautifulSoup(html_report, 'html.parser')

    story_points = int(parsed_report.find('span', class_='points').text)

    assert story_points == application_data['story_points']
