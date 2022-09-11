"""html_editor module."""
import os
from collections import namedtuple
from typing import Tuple

from bs4 import BeautifulSoup
from page_loader.url_processing import (
    generate_file_name_from_url,
    is_domains_equal,
    prepare_asset_url,
)

AssetInfo = namedtuple('AssetInfo', [
    'asset_url',
    'asset_file_name',
])

RESOURCE_TAG_WITH_LINKS = {
    'img': 'src',
    'link': 'href',
    'script': 'src',
}


def prepare_html_and_assets(
    html_content: bytes,
    page_url: str,
    assets_directory_name: str,
) -> Tuple[str, list]:
    """Prepare HTML content for using with local assets.

    Args:
        html_content (bytes): Web page HTML content int text format.
        page_url (str): URL of downloading web page.
        assets_directory_name (str): Name of directory to store assets.

    Returns:
        (Tuple[str, list]): Formatted HTML content and set of assets.
    """
    parsed_html = parse_html(html_content)

    assets = []

    for asset in parsed_html.find_all(RESOURCE_TAG_WITH_LINKS.keys()):
        asset_src = asset.get(RESOURCE_TAG_WITH_LINKS[asset.name])
        if is_domains_equal(asset_src, page_url):
            asset_url = prepare_asset_url(asset_src, page_url)
            asset_file_name = generate_file_name_from_url(asset_url)
            asset[RESOURCE_TAG_WITH_LINKS[asset.name]] = os.path.join(
                assets_directory_name,
                asset_file_name,
            )
            assets.append(AssetInfo(
                asset_url,
                asset_file_name,
            ))
    return (
        parsed_html.prettify(),
        list(set(assets)),
    )


def parse_html(html_content: bytes) -> BeautifulSoup:
    """Parse HTML content.

    Args:
        html_content (bytes):Unparsed HTML content.

    Returns:
        (BeautifulSoup): Parsed HTML content in BeautifulSoup format.
    """
    return BeautifulSoup(html_content, 'html.parser')
