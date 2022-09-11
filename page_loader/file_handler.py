"""file_handler module."""
import os
from typing import Optional, Union


def is_directory_exists(dir_path: str) -> bool:
    """Check if directory exists.

    Args:
        dir_path (str): Path to directory.

    Returns:
        (bool): True if directory exists.
    """
    return os.path.exists(dir_path)


def save_to_file(
    content_to_save: Union[str, bytes],
    output_path: str,
    file_name: str,
) -> Optional[str]:
    """Save downloaded HTML content to file.

    Args:
        content_to_save (str): HTML content to save in file.
        output_path (str): Path to directory to save file.
        file_name (str): File name to save.

    Returns:
        (Optional[str]): Full path to saved file. None in case of error.
    """
    full_path = os.path.join(
        output_path,
        file_name,
    )
    open_file_mode = 'w' if isinstance(content_to_save, str) else 'wb'
    try:
        with open(full_path, open_file_mode) as file_to_save:
            file_to_save.write(content_to_save)
    except OSError:
        return None
    return full_path


def create_assets_directory(output_path: str, directory_name: str) -> str:
    """Create directory for assets.

    Args:
        output_path (str): Path where to create directory for assets.
        directory_name (str): Name of the directory for assets.

    Returns:
        (str): Full path to new directory.
    """
    directory_full_path = os.path.join(
        output_path,
        directory_name,
    )
    try:
        os.mkdir(directory_full_path)
    except OSError:
        return None
    return directory_full_path
