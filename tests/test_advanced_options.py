import os
import subprocess

from utils.command import build_command
from utils.report import assert_story_points_from_report_file
from utils.report import assert_valid_csv


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
    custom_rule_path = os.path.join(os.getenv('PROJECT_PATH'), 'fixtures/xml', 'javax-package-custom.windup.xml')

    command = build_command(
        application_data['file_name'],
        application_data['source'],
        application_data['target'],
        **{'userRulesDirectory': custom_rule_path}
    )

    output = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, encoding='utf-8').stdout
    assert 'Report created' in output

    migration_issues_path = os.path.join(report_path, 'reports/migration_issues.html')
    assert os.path.exists(migration_issues_path) is True

    with open(migration_issues_path) as file:
        file_content = file.read()
    assert 'CUSTOM RULE for javax.* package import' in file_content
