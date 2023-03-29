import os
import subprocess

from utils.command import build_command
from utils.report import assert_story_points_from_report_file


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

    assert_story_points_from_report_file(104)

    with open(report_path + '/reports/ApplicationDetails_JEE_Example_App.html') as file:
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

    assert_story_points_from_report_file(application_data['story_points'])

    assert os.path.exists(report_path + '/reports/divareport_petclinic.html') is True
