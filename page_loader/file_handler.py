"""file_handler module."""
import os
import re
from typing import Optional
from urllib.parse import urlparse


def save_to_file(
    content_to_save: str,
    output_path: str,
    url: str,
) -> Optional[str]:
    """Save downloaded HTML content to file.

    Args:
        content_to_save (str): HTML content to save in file.
        output_path (str): Path to directory to save file.
        url (str): URL of web page to download.

    Returns:
        (Optional[str]): Full path to saved file. None in case of error.
    """
    converted_filename = convert_url_to_file_name(url)
    full_path = os.path.join(
        output_path,
        '.'.join((converted_filename, 'html')),
    )
    try:
        with open(full_path, 'w', encoding='utf-8') as file_to_save:
            file_to_save.write(content_to_save)
    except OSError:
        return None
    return full_path


def convert_url_to_file_name(url: str) -> str:
    """Convert URL to safe name for file.

    Args:
        url (str): URL of web page to download.

    Returns:
        (str): File name, converted from URL.
    """
    url_parse_result = urlparse(url)
    path_without_scheme = '{0}{1}'.format(
        url_parse_result.netloc,
        url_parse_result.path,
    )
    filename_without_extension = remove_extension(path_without_scheme)
    return replace_separation_chars_to_dashes(filename_without_extension)


def remove_extension(path_with_extension: str) -> str:
    """Remove extension from URL.

    Args:
        path_with_extension (str): Path with extension.

    Returns:
        (str): Path without extension.
    """
    splitted_filename = os.path.splitext(path_with_extension)
    return splitted_filename[0]


def replace_separation_chars_to_dashes(filename: str) -> str:
    """Replace separation characters from URL to dashes.

    Args:
        filename (str): File name needed to replace separation characters.

    Returns:
        (str): File name with replaced to dashes separation characters.
    """
    return re.sub('[^a-zA-Z0-9]', '-', filename)
