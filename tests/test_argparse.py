import os
import pytest
from unittest import mock

from page_loader.scripts.page_loader import main
from tests.helpers.utils import (
    get_fixture_path,
    read,
)


@pytest.fixture
def argparse_help_output_fixture():
    fixture_path = get_fixture_path('help_output')
    return read(fixture_path)


@pytest.fixture
def argparse_missing_page_url_arg_output_fixture():
    fixture_path = get_fixture_path('missing_page_url_arg')
    return read(fixture_path)


def test_argparse_call_help(capsys, argparse_help_output_fixture):
    try:
        with mock.patch('sys.argv', ['page_loader', '--help']):
            main()
    except SystemExit:
        pass
    captured = capsys.readouterr()
    print(argparse_help_output_fixture)
    print(captured.out)
    assert argparse_help_output_fixture in captured.out


def test_argparse_missing_page_url_arg(capsys, argparse_missing_page_url_arg_output_fixture):
    try:
        with mock.patch('sys.argv', ['page_loader']):
            main()
    except SystemExit:
        pass
    captured = capsys.readouterr()
    assert argparse_missing_page_url_arg_output_fixture == captured.err
