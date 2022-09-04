"""html_editor module."""
from bs4 import BeautifulSoup
from collections import namedtuple
from urllib.parse import urljoin, urlparse
import os
from typing import Set, Tuple

from page_loader.url_processing import (
    is_domains_equal,
    generate_file_name_from_url,
    prepare_asset_url,
)

AssetInfo = namedtuple('AssetInfo', [
    'asset_url',
    'asset_file_name',
])


def prepare_html_and_assets(
        html_content: bytes,
        page_url: str,
        assets_directory_name: str,
    ) -> Tuple[str, list]:
    """Prepare HTML content for using with local assets.
    
    Args:
        html_doc (bytes): Web page HTML content int text format.
    
    Returns:
        (Tuple[str, list]): Formatted HTML content and set of assets.
    """
    parsed_html = parse_html(html_content)

    assets = []

    for asset in parsed_html.find_all('img'):
        asset_src = asset.get('src')

        if is_domains_equal(asset_src, page_url):
            asset_url = prepare_asset_url(asset_src, page_url)
            asset_file_name = generate_file_name_from_url(asset_url)
            local_asset_path = os.path.join(
                assets_directory_name,
                asset_file_name,
            )
            asset['src'] = local_asset_path
            assets.append(AssetInfo(
                asset_url,
                asset_file_name,
            ))
    return (
        parsed_html.prettify(), 
        list(set(assets)),
    )


def parse_html(html_content: bytes) -> BeautifulSoup:
    """Parse HTML content."""
    return BeautifulSoup(html_content, 'html.parser')



