import os
import pytest

from tests.helpers.utils import (
    get_fixture_path,
    read,
)

FIXTURE_HTML_PAGE_DOWNLOADED_FILE_NAME = 'ru-hexlet-io-courses_after.html'
FIXTURE_HTML_PAGE_PROCESSED_FILE_NAME = 'ru-hexlet-io-courses_before.html'


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
