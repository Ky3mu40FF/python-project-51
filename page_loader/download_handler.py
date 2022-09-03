"""download_handler module."""
import requests


def get_page_html_content(url: str) -> str:
    """Get HTML content as a text from url.

    Args:
        url (str): URL of web page to download.

    Returns:
        (str): HTML content of web page.
    """
    response = requests.get(url)
    return response.text
