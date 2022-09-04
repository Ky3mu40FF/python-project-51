"""tests for download_handler module."""
import os
import requests_mock

from page_loader.download_handler import fetch_resource


def test_fetch_resource_html(expected_html_downloaded):
    test_url = 'https://ru.hexlet.io/courses'
    with requests_mock.Mocker() as m:
        m.get(
            test_url,
            content=expected_html_downloaded,
        )
        actual_html_downloaded = fetch_resource(test_url)
        assert expected_html_downloaded == actual_html_downloaded
