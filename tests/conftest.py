import os
import pytest

from tests.helpers.utils import (
    get_fixture_path,
    read,
)

FIXTURE_HTML_PAGE_DOWNLOADED_FILE_NAME = 'ru-hexlet-io-courses_before.html'
FIXTURE_HTML_PAGE_PROCESSED_FILE_NAME = 'ru-hexlet-io-courses_after.html'
FIXTURE_ASSET_IMAGE_FILE_NAME = 'nodejs.png'


@pytest.fixture()
def expected_html_downloaded():
    return read(
        get_fixture_path(FIXTURE_HTML_PAGE_DOWNLOADED_FILE_NAME),
        'rb',
    )


@pytest.fixture()
def expected_html_processed():
    return read(
        get_fixture_path(FIXTURE_HTML_PAGE_PROCESSED_FILE_NAME),
        'rb',
    )


@pytest.fixture()
def expected_asset_image():
    return read(
        get_fixture_path(FIXTURE_ASSET_IMAGE_FILE_NAME),
        'rb',
    )
