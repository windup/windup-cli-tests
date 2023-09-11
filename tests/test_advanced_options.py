import json
import os
import subprocess

from bs4 import BeautifulSoup

from utils.command import build_command
from utils.report import assert_story_points_from_report_file
from utils.report import assert_valid_csv
from zipfile import ZipFile


def test_skip_report(analysis_data):
    application_data = analysis_data['jee_example_app']
    report_path = os.getenv('REPORT_OUTPUT_PATH')

    command = build_command(
        application_data['file_name'],
        application_data['source'],
        application_data['target'],
        **{'skipReports': ''}
    )

    output = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, encoding='utf-8').stdout

    assert 'Generating reports were disabled' in output

    assert os.path.exists(report_path + '/index.html') is False
    assert os.path.exists(report_path + '/stats/detailed_stats.csv') is True


def test_analyze_known_libraries(analysis_data):
    application_data = analysis_data['jee_example_app']
    report_path = os.getenv('REPORT_OUTPUT_PATH')

    command = build_command(
        application_data['file_name'],
        application_data['source'],
        application_data['target'],
        **{'analyzeKnownLibraries': ''}
    )

    output = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, encoding='utf-8').stdout

    assert 'Report created' in output

    assert_story_points_from_report_file()

    with open(report_path + '/api/files.json') as file:
        report_detail = file.read()

    assert 'org.apache.log4j' in report_detail


def test_transaction_analysis(analysis_data):
    application_data = analysis_data['spring_petclinic']
    report_path = os.getenv('REPORT_OUTPUT_PATH')

    command = build_command(
        application_data['file_name'],
        application_data['source'],
        application_data['target'],
        **{'enableTransactionAnalysis': ''}
    )

    output = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, encoding='utf-8').stdout

    assert 'Report created' in output

    assert_story_points_from_report_file()

    with open(report_path + '/api/transactions.json', 'r') as file:
        json_data = json.load(file)

    assert len(json_data[0]["transactions"]) > 0


def test_csv_report(analysis_data):
    application_data = analysis_data['jee_example_app']
    report_path = os.getenv('REPORT_OUTPUT_PATH')

    command = build_command(
        application_data['file_name'],
        application_data['source'],
        application_data['target'],
        **{'exportCSV': ''}
    )
    output = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, encoding='utf-8').stdout

    assert 'Report created' in output

    assert_valid_csv(os.path.join(report_path, 'AllIssues.csv'))
    assert_valid_csv(os.path.join(report_path, 'ApplicationFileTechnologies.csv'))
    assert_valid_csv(os.path.join(report_path, 'jee_example_app_1_0_0_ear.csv'))


def test_custom_rules_analysis(analysis_data):
    application_data = analysis_data['complete_duke']
    report_path = os.getenv('REPORT_OUTPUT_PATH')
    custom_rule_path = os.path.join(os.getenv('PROJECT_PATH'), 'data/xml', 'javax-package-custom.windup.xml')

    command = build_command(
        application_data['file_name'],
        application_data['source'],
        application_data['target'],
        **{'userRulesDirectory': custom_rule_path}
    )

    output = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, encoding='utf-8').stdout
    assert 'Report created' in output

    with open(report_path + '/api/issues.json') as file:
        file_content = file.read()

    assert 'CUSTOM RULE for javax.* package import' in file_content

def test_legacy_report(analysis_data):
    application_data = analysis_data['jee_example_app']
    report_path = os.getenv('REPORT_OUTPUT_PATH')

    command = build_command(
        application_data['file_name'],
        application_data['source'],
        application_data['target'],
        **{'legacyReports': ''}
    )
    output = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, encoding='utf-8').stdout

    assert 'Report created' in output

    assert os.path.exists(report_path + '/reports') is True
    assert os.path.exists(report_path + '/stats') is True

    with open(report_path + "/index.html") as file:
        html_report = file.read()
    parsed_report = BeautifulSoup(html_report, 'html.parser')

    report_story_points = int(parsed_report.find('span', class_='points').text)

    assert report_story_points == application_data['story_points']

def test_skip_source_code_reports(analysis_data):
    application_data = analysis_data['administracion_efectivo']
    report_path = os.getenv('REPORT_OUTPUT_PATH')

    command = build_command(
        application_data['file_name'],
        application_data['source'],
        application_data['target'],
        **{'skipSourceCodeReports': ''}
    )

    output = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, encoding='utf-8').stdout

    assert 'Report created' in output

    assert os.path.exists(report_path + '/api') is True
    assert os.path.exists(report_path + '/api/files') is False


def test_export_zip_report(analysis_data):
    application_data = analysis_data['jee_example_app']
    report_path = os.getenv('REPORT_OUTPUT_PATH')
    zip_report_path = os.path.join(report_path, 'reports.zip')
    unzipped_report_path = os.path.join(report_path, 'unzippedReport')

    command = build_command(
        application_data['file_name'],
        application_data['source'],
        application_data['target'],
        **{'exportZipReport': ''}
    )
    output = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, encoding='utf-8').stdout

    assert 'Report created' in output

    assert os.path.exists(zip_report_path) is True

    with ZipFile(zip_report_path, 'r') as zip_file:
        zip_file.extractall(unzipped_report_path)

    assert_story_points_from_report_file(**{'report_path': unzipped_report_path})
