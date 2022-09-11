"""tests for page_loader module."""
import os
import requests_mock
import tempfile

from page_loader.page_loader import download
from tests.helpers.utils import read

HTML = 'html'
IMG = 'img'
STYLE = 'style'
SCRIPT = 'script'
ASSETS_DIRECTORY = 'assets_directory'

RESOURCE_URLS = {
    'html': 'https://ru.hexlet.io/courses',
    'img': 'https://ru.hexlet.io/assets/professions/nodejs.png',
    'style': 'https://ru.hexlet.io/assets/application.css',
    'script': 'https://ru.hexlet.io/packs/js/runtime.js',
}

EXPECTED_NAMES = {
    'html': 'ru-hexlet-io-courses.html',
    'assets_directory': 'ru-hexlet-io-courses_files',
    'img': 'ru-hexlet-io-assets-professions-nodejs.png',
    'style': 'ru-hexlet-io-assets-application.css',
    'script': 'ru-hexlet-io-packs-js-runtime.js',
}


def test_download(
    expected_html_downloaded,
    expected_html_processed,
    expected_asset_image,
    expected_asset_style,
    expected_asset_script,
):
    with requests_mock.Mocker() as m:
        m.get(
            url=RESOURCE_URLS[HTML],
            content=expected_html_downloaded,
        )
        m.get(
            url=RESOURCE_URLS[IMG],
            content=expected_asset_image,
        )
        m.get(
            url=RESOURCE_URLS[STYLE],
            content=expected_asset_style,
        )
        m.get(
            url=RESOURCE_URLS[SCRIPT],
            content=expected_asset_script,
        )
        with tempfile.TemporaryDirectory() as tmpdirname:
            expected_html_file_full_path = os.path.join(tmpdirname, EXPECTED_NAMES[HTML])
            expected_assets_directory_full_path = os.path.join(tmpdirname, EXPECTED_NAMES[ASSETS_DIRECTORY])
            expected_asset_image_full_path = os.path.join(expected_assets_directory_full_path, EXPECTED_NAMES[IMG])
            expected_asset_style_full_path = os.path.join(expected_assets_directory_full_path, EXPECTED_NAMES[STYLE])
            expected_asset_script_full_path = os.path.join(expected_assets_directory_full_path, EXPECTED_NAMES[SCRIPT])
            
            actual_full_path = download(
                page_url=RESOURCE_URLS[HTML],
                output_path=tmpdirname,
            )

            actual_html_content = read(actual_full_path, 'rb')
            actual_asset_image = read(expected_asset_image_full_path, 'rb')
            actual_asset_style = read(expected_asset_style_full_path, 'rb')
            actual_asset_script = read(expected_asset_script_full_path, 'rb')

            assert expected_html_file_full_path == actual_full_path
            assert expected_html_processed == actual_html_content
            assert os.path.isdir(expected_assets_directory_full_path)
            assert os.path.isfile(expected_asset_image_full_path)
            assert os.path.isfile(expected_asset_style_full_path)
            assert os.path.isfile(expected_asset_script_full_path)
            assert expected_asset_image == actual_asset_image
            assert expected_asset_style == actual_asset_style
            assert expected_asset_script == actual_asset_script