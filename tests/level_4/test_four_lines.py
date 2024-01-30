from functions.level_4.four_lines_counter import count_lines_in
from unittest.mock import patch, mock_open
import pytest
import os



def test__count_lines_in__nonexistent_file():
    with patch('builtins.open', side_effect=FileNotFoundError):
        result = count_lines_in('nonexistent_file.txt')
    assert result is None

@pytest.mark.parametrize('filepath', [
    (['1', '2', '3', '4'], 4),
    (['1', '#2', '3', '4'], 3),
    (['#1', '#2', '#3', '#4'], 0),
    ([], 0),
    (['', '', ''], 3)
], indirect=True)
def test__count_lines_in(filepath):
    filepath, expected_result = filepath
    assert count_lines_in(filepath) == expected_result


def test__count_lines_in__nonexistent_file_vesr2():
    with patch('builtins.open', side_effect=FileNotFoundError):
        assert count_lines_in('no_file.txt') is None
