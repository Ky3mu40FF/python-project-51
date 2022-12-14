"""download_handler module."""
import requests
from page_loader.file_handler import save_to_file
from page_loader.logging import get_logger
from progress.bar import Bar

logger = get_logger(__name__)


def fetch_resource(url: str) -> bytes:
    """Fetch resource from URL.

    Args:
        url (str): URL of resource.

    Returns:
        (bytes): Resource content.

    Raises:
        requests.exceptions.RequestException: If request error status.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as req_exception:
        logger.error("Can't download resource at URL {0}\n{1}".format(
            url,
            req_exception,
        ))
        logger.debug(req_exception, exc_info=True)
        raise
    return response.content


def download_assets(output_path: str, assets: list) -> None:
    """Download assets and save to files.

    Args:
        output_path (str): Path where to save downloaded assets.
        assets (list): List of assets to download.
    """
    logger.info('Assets downloading started.')
    with Bar('Downloading assets', max=len(assets)) as assets_download_bar:
        for asset in assets:
            logger.debug('Downloading resource {0}'.format(asset.asset_url))
            try:
                asset_content = fetch_resource(asset.asset_url)
            except requests.exceptions.RequestException:
                logger.info('Skipping asset {0}'.format(asset.asset_url))
                continue
            save_to_file(
                content_to_save=asset_content,
                output_path=output_path,
                file_name=asset.asset_file_name,
            )
            assets_download_bar.next()
    logger.info('Assets downloading finished.')
