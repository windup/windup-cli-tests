import os
import subprocess

from utils.command import build_command
from utils.report import assert_story_points_from_report_file


def test_invalid_target(analysis_data):
    application_data = analysis_data['jee_example_app']

    target = 'invalidTarget'
    command = build_command(
        application_data['file_name'],
        application_data['source'],
        target
    )

    output = subprocess.run(command, shell=True, check=True, stderr=subprocess.PIPE, encoding='utf-8').stderr

    assert 'ERROR: target value (' + target + ') not found' in output
