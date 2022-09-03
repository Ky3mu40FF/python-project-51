import os
import pytest


def get_fixture_path(name: str) -> str:
    return os.path.join('tests/fixtures', name)


def read(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        result = f.read()
    return result

fixture_page_file_name = 'expected_ru-hexlet-io-courses.html'
fixture_page_file_path = get_fixture_path(fixture_page_file_name)


@pytest.fixture()
def expected_html_content():
    return read(fixture_page_file_path)