"""tests for file_handler module."""
import os
import tempfile

from page_loader.file_handler import save_to_file


def read(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        result = f.read()
    return result


def test_save_to_file(expected_html_content):
    test_url = 'https://ru.hexlet.io/courses'
    expected_file_name = 'ru-hexlet-io-courses.html'
    with tempfile.TemporaryDirectory() as tmpdirname:
        expected_full_path = os.path.join(tmpdirname, expected_file_name)
        actual_full_path = save_to_file(
            content_to_save=expected_html_content,
            output_path=tmpdirname,
            url=test_url,
        )
        actual_html_content = read(actual_full_path)
        assert expected_full_path == actual_full_path
        assert expected_html_content == actual_html_content


def test_save_to_file_not_exists_directory():
    actual_result = save_to_file(
        content_to_save='',
        output_path='/not/exists',
        url='www.test.ru/test.html',
    )
    assert actual_result is None
