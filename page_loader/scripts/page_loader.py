#!/usr/bin/env python3
"""page_loader main module."""

import argparse
import os
import sys

import requests
from page_loader.page_loader import download


def parse_args():
    """Parse input arguments.

    Returns:
        (any): Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description='Downloads web page with all content.',
    )
    parser.add_argument('page_url')
    parser.add_argument(
        '-o',
        '--output',
        help='Path to save downloaded page. Default - current working directory.',
        default=os.getcwd(),
    )
    return parser.parse_args()


def main():
    """page_loader entry point."""
    args = parse_args()
    try:
        page_output_path = download(
            args.page_url,
            args.output,
        )
    except (requests.exceptions.RequestException, OSError):
        sys.exit(1)
    print('Page ({0}) successfully saved to {1}'.format(
        args.page_url,
        page_output_path,
    ))


if __name__ == '__main__':
    main()
