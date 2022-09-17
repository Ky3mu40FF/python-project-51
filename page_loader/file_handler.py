"""file_handler module."""
import os
from typing import Optional, Union

from page_loader.logging import get_logger

logger = get_logger(__name__)


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

    Raises:
        OSError: If can't save file.
    """
    full_path = os.path.join(
        output_path,
        file_name,
    )
    open_file_mode = 'w' if isinstance(content_to_save, str) else 'wb'
    logger.info('Saving file: {0}'.format(full_path))
    try:
        with open(full_path, open_file_mode) as file_to_save:
            file_to_save.write(content_to_save)
    except OSError as write_file_exception:
        logger.warning("Can't save file {0}".format(full_path))
        logger.debug(write_file_exception, exc_info=True)
        raise
    return full_path


def create_assets_directory(output_path: str, directory_name: str) -> str:
    """Create directory for assets.

    Args:
        output_path (str): Path where to create directory for assets.
        directory_name (str): Name of the directory for assets.

    Returns:
        (str): Full path to new directory.

    Raises:
        OSError: If can't create assets directory.
    """
    directory_full_path = os.path.join(
        output_path,
        directory_name,
    )
    logger.info('Creating assets directory: {0}'.format(directory_full_path))
    try:
        os.mkdir(directory_full_path)
    except OSError as assets_mkdir_exception:
        logger.warning("Can't create assets directory {0}".format(
            directory_full_path,
        ))
        logger.debug(assets_mkdir_exception, exc_info=True)
        raise
    return directory_full_path
