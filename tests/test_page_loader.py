"""tests for page_loader module."""
import os
import pytest
from requests import RequestException
import requests_mock
import tempfile

from page_loader.page_loader import download
from tests.fixture_files_extra_functions.fixture_file_read import read_as_binary

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


@pytest.fixture
def tempdir():
    return tempfile.mkdtemp()


def test_download(
    tempdir,
    requests_mock,
    expected_html_downloaded,
    expected_html_processed,
    expected_asset_image,
    expected_asset_style,
    expected_asset_script,
):
    requests_mock.get(
        url=RESOURCE_URLS[HTML],
        content=expected_html_downloaded,
    )
    requests_mock.get(
        url=RESOURCE_URLS[IMG],
        content=expected_asset_image,
    )
    requests_mock.get(
        url=RESOURCE_URLS[STYLE],
        content=expected_asset_style,
    )
    requests_mock.get(
        url=RESOURCE_URLS[SCRIPT],
        content=expected_asset_script,
    )
    expected_html_file_full_path = os.path.join(tempdir, EXPECTED_NAMES[HTML])
    expected_assets_directory_full_path = os.path.join(tempdir, EXPECTED_NAMES[ASSETS_DIRECTORY])
    expected_asset_image_full_path = os.path.join(expected_assets_directory_full_path, EXPECTED_NAMES[IMG])
    expected_asset_style_full_path = os.path.join(expected_assets_directory_full_path, EXPECTED_NAMES[STYLE])
    expected_asset_script_full_path = os.path.join(expected_assets_directory_full_path, EXPECTED_NAMES[SCRIPT])
    
    actual_full_path = download(
        page_url=RESOURCE_URLS[HTML],
        output_path=tempdir,
    )

    assert expected_html_file_full_path == actual_full_path
    assert expected_html_processed == read_as_binary(actual_full_path)
    assert expected_asset_image == read_as_binary(expected_asset_image_full_path)
    assert expected_asset_style == read_as_binary(expected_asset_style_full_path)
    assert expected_asset_script == read_as_binary(expected_asset_script_full_path)


def test_output_directory_exists():
    not_existing_dir = '/this/dir/not/exists'
    with pytest.raises(FileNotFoundError) as exc_info:
        download(
            page_url=RESOURCE_URLS[HTML],
            output_path=not_existing_dir,
        )
        assert "Output directory not found: {0}".format(not_existing_dir) in str(exc_info.value)


def test_cant_create_assets_directory(
    tempdir,
    requests_mock,
    expected_html_downloaded,
):
    requests_mock.get(
        url=RESOURCE_URLS[HTML],
        content=expected_html_downloaded,
    )
    assets_directory_full_path = os.path.join(
        tempdir,
        EXPECTED_NAMES[ASSETS_DIRECTORY],
    )
    os.mkdir(assets_directory_full_path)
    with pytest.raises(FileExistsError) as exc_info:
        download(
            page_url=RESOURCE_URLS[HTML],
            output_path=tempdir,
        )
        assert "Can't create assets directory {0}".format(assets_directory_full_path)


def test_resource_not_found(tempdir, requests_mock):
    requests_mock.get(
        url=RESOURCE_URLS[HTML],
        status_code=404,
    )
    with pytest.raises(RequestException) as exc_info:
        download(
            page_url=RESOURCE_URLS[HTML],
            output_path=tempdir,
        )
        assert "Can't download resource at URL: {0}".format(RESOURCE_URLS[HTML])


def test_request_timeout(tempdir, requests_mock):
    requests_mock.get(
        url=RESOURCE_URLS[HTML],
        status_code=408,
    )
    with pytest.raises(RequestException) as exc_info:
        download(
            page_url=RESOURCE_URLS[HTML],
            output_path=tempdir,
        )
        assert "Can't download resource at URL: {0}".format(RESOURCE_URLS[HTML])


def test_internal_server_error(tempdir, requests_mock):
    requests_mock.get(
        url=RESOURCE_URLS[HTML],
        status_code=500,
    )
    with pytest.raises(RequestException) as exc_info:
        download(
            page_url=RESOURCE_URLS[HTML],
            output_path=tempdir,
        )
        assert "Can't download resource at URL: {0}".format(RESOURCE_URLS[HTML])
