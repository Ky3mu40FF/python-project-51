"""tests for page_loader module."""
import os
import requests_mock
import tempfile

from page_loader.page_loader import download


def read(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        result = f.read()
    return result


def test_download(expected_html_content):
    test_url = 'https://ru.hexlet.io/courses'
    expected_file_name = 'ru-hexlet-io-courses.html'
    with requests_mock.Mocker() as m:
        m.get(
            test_url,
            status_code = 200,
            text=expected_html_content,
        )
        with tempfile.TemporaryDirectory() as tmpdirname:
            expected_full_path = os.path.join(tmpdirname, expected_file_name)
            actual_full_path = download(
                url=test_url,
                output_path=tmpdirname,
            )
            actual_html_content = read(actual_full_path)
            assert expected_full_path == actual_full_path
            assert expected_html_content == actual_html_content