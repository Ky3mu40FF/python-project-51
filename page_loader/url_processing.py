"""Page Loader url_processing module."""

import os
import re
from typing import Tuple
from urllib.parse import urljoin, urlparse

HTML_FILE_EXTENSION = '.html'
ASSETS_DIRECTORY_SUFFIX = '_files'


def is_domains_equal(asset_url: str, page_url: str) -> bool:
    """Check if domain of asset equal to domain of web page."""
    asset_hostname = urlparse(asset_url).hostname
    page_hostname = urlparse(page_url).hostname
    return not asset_hostname or asset_hostname == page_hostname


def prepare_asset_url(asset_url: str, page_url: str) -> str:
    """Prepare assert url if it's not absolute."""
    return urljoin(page_url, asset_url)


def generate_assets_directory_name(page_url: str) -> str:
    hostname, path = get_hostname_and_path(page_url)
    path_without_extension, _ = os.path.splitext(path)
    file_name = os.path.join(
        hostname,
        path_without_extension.strip('/'),
    )
    return '{0}{1}'.format(
        re.sub(r'\W', '-', file_name),
        ASSETS_DIRECTORY_SUFFIX,
    )


def generate_file_name_from_url(resource_url) -> str:
    hostname, path = get_hostname_and_path(resource_url)
    path_without_extension, extension = os.path.splitext(path)
    file_name = os.path.join(
        hostname,
        path_without_extension.strip('/'),
    )
    return '{0}{1}'.format(
        re.sub(r'\W', '-', file_name),
        extension if extension else HTML_FILE_EXTENSION,
    )
    

def get_hostname_and_path(url: str) -> Tuple[str, str]:
    """Get hostname and path from URL."""
    parsed_url = urlparse(url)
    return (parsed_url.hostname, parsed_url.path)
