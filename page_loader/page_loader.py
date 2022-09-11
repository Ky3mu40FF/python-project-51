"""page_loader module."""
from typing import Optional

from page_loader.download_handler import download_assets, fetch_resource
from page_loader.file_handler import (
    create_assets_directory,
    is_directory_exists,
    save_to_file,
)
from page_loader.html_processing import prepare_html_and_assets
from page_loader.url_processing import (
    generate_assets_directory_name,
    generate_file_name_from_url,
)


def download(page_url: str, output_path: str) -> Optional[str]:
    """Download web page from URL to output_path.

    Args:
        page_url (str): URL of web page to download.
        output_path (str): Path to directory to save result of downloading.

    Returns:
        (Optional[str]): Full path to downloaded web page.
    """
    if not is_directory_exists(output_path):
        return None

    page_content = fetch_resource(page_url)

    assets_directory_name = generate_assets_directory_name(page_url)

    assets_directory_path = create_assets_directory(
        output_path,
        assets_directory_name,
    )

    prepared_html, assets = prepare_html_and_assets(
        html_content=page_content,
        page_url=page_url,
        assets_directory_name=assets_directory_name,
    )

    download_assets(
        output_path=assets_directory_path,
        assets=assets,
    )

    return save_to_file(
        content_to_save=prepared_html,
        output_path=output_path,
        file_name=generate_file_name_from_url(page_url),
    )
