import csv
import json
import os

from bs4 import BeautifulSoup


def assert_story_points_from_report_file(story_points, **kwargs):
    """
    Asserts that the story points in the report file match the provided value.

    Args:
        story_points (int): The expected story points value to match.
        **kwargs: Optional keyword arguments.
            report_path (str): The path to the report file. If not provided,
                the function will use the value of the 'REPORT_OUTPUT_PATH' environment variable.

    Raises:
        AssertionError: If the story points in the report file do not match the provided value.

    Returns:
        None.

    """
    report_path = os.getenv('REPORT_OUTPUT_PATH')
    report_path = kwargs.get('report_path', report_path)

    with open(report_path + "/api/applications.json") as file:
        json_data = json.load(file)

    assert json_data[0]['storyPoints'] == story_points


def assert_valid_csv(csv_file_path, **kwargs):
    """
        Asserts that the given CSV file is valid.
        A CSV file is considered valid if it exists and all of its rows have the same number of columns.

        Args:
            csv_file_path (str): The file path of the CSV file to validate.
            **kwargs: Optional keyword arguments.
                delimiter (str): The delimiter used in the CSV file. Defaults to ','.

        Raises:
            AssertionError: If the CSV file does not exist or if its rows have different numbers of columns.

        Returns:
            None.
    """
    assert os.path.exists(csv_file_path) is True
    delimiter = kwargs.get('delimiter', ',')

    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=delimiter)
        columns_number = len(next(csv_reader))
        assert all(len(row) == columns_number for row in csv_reader) is True
