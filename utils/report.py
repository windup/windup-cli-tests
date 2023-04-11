import csv
import os

from bs4 import BeautifulSoup


def assert_story_points_from_report_file(story_points):
    report_path = os.getenv('REPORT_OUTPUT_PATH')

    with open(report_path + "/index.html") as file:
        html_report = file.read()
    parsed_report = BeautifulSoup(html_report, 'html.parser')

    report_story_points = int(parsed_report.find('span', class_='points').text)

    assert report_story_points == story_points


def assert_valid_csv(csv_file_path, **kwargs):
    """
        Asserts that the given CSV file is valid.
        A CSV file is considered valid if it exists and all of its rows have the same number of columns.

        Args:
            csv_file_path (str): The file path of the CSV file to validate.
            **kwargs (str): Optional keyword arguments.
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
