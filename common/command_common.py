import os


def build_command(binary_path, source, target, **kwargs):
    """
        Builds a command for executing windup

        Args:
            binary_path (str): Path to the binary file of the application to be analyzed.
            source (str): Source of the application.
            target (str): Target for the application to migrate to.
            **kwargs (str): Optional keyword arguments to be passed to Windup as additional options.
                this argument takes a dict, where each key is the argument, which can be passed with or without the '--'

        Returns:
            str: The full command to execute with the specified options and arguments.

        Raises:
            Exception: If `binary_path` is not provided.
    """
    windup_path = os.getenv('WINDUP_CLI_PATH')
    report_path = os.getenv('REPORT_OUTPUT_PATH')
    if not binary_path:
        raise Exception('Binary path is required')

    command = windup_path + ' --overwrite -b --input ' + binary_path + ' --output ' + report_path

    if source:
        command += ' --source ' + source

    if target:
        command += ' --target ' + target

    for key, value in kwargs.items():
        if '--' not in key:
            key = '--' + key
        command += ' ' + key + ' ' + value

    return command
