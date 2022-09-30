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
    except requests.exceptions.RequestException as req_exc:
        print('Error occured while downloading. {0}'.format(req_exc))
        sys.exit(1)
    except OSError as os_exc:
        print('Error occured while saving to file. {0}\n{1}'.format(os_exc.strerror, os_exc.filename))
        sys.exit(1)
    except Exception as exc:
        print('Unexpected error occured. {0}'.format(exc))
        sys.exit(1)
    print('Page {0} successfully saved to {1}'.format(
        args.page_url,
        page_output_path,
    ))


if __name__ == '__main__':
    main()
