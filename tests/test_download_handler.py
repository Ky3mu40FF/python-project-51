"""tests for download_handler package."""
import os
import requests_mock

from page_loader.download_handler import get_page_html_content


def read(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        result = f.read()
    return result


def test_get_web_page(expected_html_content):
    test_url = 'https://ru.hexlet.io/courses'
    with requests_mock.Mocker() as m:
        m.get(
            test_url,
            status_code = 200,
            text=expected_html_content,
        )
        actual_html_content = get_page_html_content(test_url)
        assert expected_html_content == actual_html_content

