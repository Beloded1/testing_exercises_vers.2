import pytest
from functions.level_4.one_brackets import delete_remove_brackets_quotes



@pytest.mark.parametrize(
        'name, expected_result',
        [
            ('{ name }', 'name'),
            ('{name}', 'am'),
            ('{ Name}', 'Nam')
        ]
)
def test__delete_remove_brackets_quotes__input_with_brackets(name, expected_result):
    assert delete_remove_brackets_quotes(name) == expected_result


def test__delete_remove_brackets_quotes__if_get_input_with_brackets():
    assert delete_remove_brackets_quotes('{ Иван }') == 'Иван'


def test__delete_remove_brackets_quotes__if_get_input_without_brackets():
    assert delete_remove_brackets_quotes(' Иван ') == ' Иван '


def test__delete_remove_brackets_quotes__if_get_an_empty_imput():
    with pytest.raises(IndexError):
        delete_remove_brackets_quotes('')
