"""page_loader.logging module."""
import logging
import sys


def get_logger(name: str) -> logging.Logger:
    """Get configured logger.

    Args:
        name (str): Logger name.

    Returns:
        (logging.Logger): Configured logger instance.
    """
    logger = logging.getLogger(name=name)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(logging.Formatter(
        fmt='[%(asctime)s: %(levelname)s] %(message)s',
    ))
    logger.addHandler(handler)

    return logger
