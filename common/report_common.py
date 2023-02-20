import os

from bs4 import BeautifulSoup


def assert_story_points_from_report_file(story_points):
    report_path = os.getenv('REPORT_OUTPUT_PATH')

    with open(report_path + "/index.html") as file:
        html_report = file.read()
    parsed_report = BeautifulSoup(html_report, 'html.parser')

    report_story_points = int(parsed_report.find('span', class_='points').text)

    assert report_story_points == story_points
