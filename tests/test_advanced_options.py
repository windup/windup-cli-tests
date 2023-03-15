import os
import subprocess

from utils.command import build_command


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
