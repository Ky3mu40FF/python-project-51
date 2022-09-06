"""tests for page_loader module."""
import os
import requests_mock
import tempfile

from page_loader.page_loader import download
from tests.helpers.utils import read


def test_download(expected_html_downloaded, expected_html_processed, expected_asset_image):
    html_page_url = 'https://ru.hexlet.io/courses'
    asset_image_url = 'https://ru.hexlet.io/assets/professions/nodejs.png'
    expected_html_file_name = 'ru-hexlet-io-courses.html'
    expected_assets_directory_name = 'ru-hexlet-io-courses_files'
    expected_asset_image_file_name = 'ru-hexlet-io-assets-professions-nodejs.png'
    with requests_mock.Mocker() as m:
        m.get(
            html_page_url,
            status_code=200,
            content=expected_html_downloaded,
        )
        m.get(
            asset_image_url,
            status_code=200,
            content=expected_asset_image,
        )
        with tempfile.TemporaryDirectory() as tmpdirname:
            expected_html_file_full_path = os.path.join(tmpdirname, expected_html_file_name)
            expected_assets_directory_full_path = os.path.join(tmpdirname, expected_assets_directory_name)
            expected_asset_image_full_path = os.path.join(expected_assets_directory_full_path, expected_asset_image_file_name)
            actual_full_path = download(
                page_url=html_page_url,
                output_path=tmpdirname,
            )
            actual_html_content = read(actual_full_path, 'rb')
            actual_asset_image = read(expected_asset_image_full_path, 'rb')
            assert expected_html_file_full_path == actual_full_path
            assert expected_html_processed == actual_html_content
            assert os.path.isdir(expected_assets_directory_full_path)
            assert os.path.isfile(expected_asset_image_full_path)
            assert expected_asset_image == actual_asset_image