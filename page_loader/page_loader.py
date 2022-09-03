"""page_loader module."""

from page_loader.download_handler import get_page_html_content
from page_loader.file_handler import save_to_file


def download(url: str, output_path: str) -> str:
    """Download web page from URL to output_path.

    Args:
        url (str): URL of web page to download.
        output_path (str): Path to directory to save result of downloading.

    Returns:
        (str): Full path to downloaded web page.
    """
    page_content = get_page_html_content(url)
    return save_to_file(page_content, output_path, url)
