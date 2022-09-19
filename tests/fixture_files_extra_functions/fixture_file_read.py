"""tests.fixture_files_extra_functions.fixture_file_read module."""
import os

def get_fixture_path(name: str) -> str:
    return os.path.join('tests/fixtures', name)


def read(file_path: str, mode: str='r'):
    with open(file_path, mode) as f:
        result = f.read()
    return result
