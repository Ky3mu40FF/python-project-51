"""file_handler module."""
import os
import re
from urllib.parse import urlparse


def save_to_file(content: str, output_path: str, url: str) -> str:
    converted_filename = convert_url_to_file_name(url)
    return os.path.join(output_path, converted_filename)


def convert_url_to_file_name(url: str) -> str:
    url_parse_result = urlparse(url)
    path_without_scheme = '{0}{1}'.format(
        url_parse_result.netloc,
        url_parse_result.path,
    )
    filename_without_extension = remove_extension(path_without_scheme)
    return replace_separation_chars_to_dashes(filename_without_extension)


def remove_extension(filename_with_extension: str) -> str:
    splitted_filename = os.path.splitext(filename_with_extension)
    if splitted_filename[-1] == '.html':
        return ''.join(splitted_filename[:-1])
    return filename_with_extension


def replace_separation_chars_to_dashes(filename: str) -> str:
    return re.sub(r'[^a-zA-Z0-9]', '-', filename)

