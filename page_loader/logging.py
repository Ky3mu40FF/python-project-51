"""page_loader.logging module."""
import logging
import os
import sys
from tempfile import gettempdir

LOG_CONSOLE_TEMPLATE = '%(message)s'
LOG_FILE_TEMPLATE = '[%(asctime)s: %(name)s - %(levelname)s] %(message)s'


class InfoFilter(logging.Filter):
    """Class for filter all non info and debug log records."""

    def filter(self, record: logging.LogRecord) -> bool:
        """Filter log records. Keep info and debug levels only.

        Args:
            record (LogRecord): Log records to filter.

        Returns:
            (bool): True if log record should be kept. False otherwise.
        """
        return record.levelno in {logging.DEBUG, logging.INFO}


def get_logger(name: str) -> logging.Logger:
    """Get configured logger.

    Args:
        name (str): Logger name.

    Returns:
        (logging.Logger): Configured logger instance.
    """
    logger = logging.getLogger(name=name)
    logger.setLevel(logging.INFO)

    stdout_handler = logging.StreamHandler(stream=sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.addFilter(InfoFilter())
    stdout_handler.setFormatter(logging.Formatter(fmt=LOG_CONSOLE_TEMPLATE))

    stderr_handler = logging.StreamHandler(stream=sys.stderr)
    stderr_handler.setLevel(logging.WARNING)
    stderr_handler.setFormatter(logging.Formatter(fmt=LOG_CONSOLE_TEMPLATE))

    os_tmp_dir = gettempdir()
    log_output = os.path.join(os_tmp_dir, 'page_loader.log')

    file_handler = logging.FileHandler(
        filename=log_output,
        mode='a',
        encoding='utf-8',
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(fmt=LOG_FILE_TEMPLATE))

    logger.handlers = [
        stdout_handler,
        stderr_handler,
        file_handler,
    ]

    return logger
