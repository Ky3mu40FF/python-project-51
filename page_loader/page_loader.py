"""page_loader module."""

from page_loader.file_handler import save_to_file


def download(url: str, output_path: str) -> str:
    """Download web page from URL to output_path.

    Args:
        url (str): URL of web page to download.
        output_path (str): Path to directory to save result of downloading.

    Returns:
        (str): Full path to downloaded web page.
    """
    full_path = save_to_file('', output_path, url)
    return 'URL: {0}\nOutput Path: {1}\nResult: {2}'.format(url, output_path, full_path)
