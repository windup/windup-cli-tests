import subprocess

from utils.command import build_command

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
