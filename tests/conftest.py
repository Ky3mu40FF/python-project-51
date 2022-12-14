import pytest

from tests.fixture_files_extra_functions.fixture_file_read import (
    get_fixture_path,
    read_as_binary,
)

FIXTURE_HTML_PAGE_DOWNLOADED_FILE_NAME = 'ru-hexlet-io-courses_before.html'
FIXTURE_HTML_PAGE_PROCESSED_FILE_NAME = 'ru-hexlet-io-courses_after.html'
FIXTURE_ASSET_IMAGE_FILE_NAME = 'nodejs.png'
FIXTURE_ASSET_STYLE_FILE_NAME = 'application.css'
FIXTURE_ASSET_SCRIPT_FILE_NAME = 'runtime.js'


@pytest.fixture()
def expected_html_downloaded():
    return read_as_binary(get_fixture_path(FIXTURE_HTML_PAGE_DOWNLOADED_FILE_NAME))


@pytest.fixture()
def expected_html_processed():
    return read_as_binary(get_fixture_path(FIXTURE_HTML_PAGE_PROCESSED_FILE_NAME))


@pytest.fixture()
def expected_asset_image():
    return read_as_binary(get_fixture_path(FIXTURE_ASSET_IMAGE_FILE_NAME))


@pytest.fixture()
def expected_asset_style():
    return read_as_binary(get_fixture_path(FIXTURE_ASSET_STYLE_FILE_NAME))


@pytest.fixture()
def expected_asset_script():
    return read_as_binary(get_fixture_path(FIXTURE_ASSET_SCRIPT_FILE_NAME))
