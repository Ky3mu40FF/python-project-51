"""download_handler module."""
import requests
from page_loader.file_handler import save_to_file


def fetch_resource(url: str) -> bytes:
    """Fetch resource from URL.

    Args:
        url (str): URL of resource.

    Returns:
        (bytes): Resource content.
    """
    response = requests.get(url)
    return response.content


def download_assets(output_path: str, assets: list) -> None:
    """Download assets and save to files.

    Args:
        output_path (str): Path where to save downloaded assets.
        assets (list): List of assets to download.
    """
    for asset in assets:
        asset_content = fetch_resource(asset.asset_url)
        save_to_file(
            content_to_save=asset_content,
            output_path=output_path,
            file_name=asset.asset_file_name,
        )
