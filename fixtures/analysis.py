import json
import pytest


@pytest.fixture(scope="session")
def json_analysis():
    with open('../data/analysis.json', 'r') as file:
        json_list = json.load(file)
    return {value['app_name']: value for value in json_list}
