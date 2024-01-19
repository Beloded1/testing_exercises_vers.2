from functions.level_2.five_replace_word import replace_word
import pytest


def test__replace_word__is_valid_input():
    assert replace_word('Hello world!', 'Hello', 'world') == 'world world!'


def test__replace_word__is_not_replace_to():
    with pytest.raises(TypeError):
        replace_word("It doesn't work", "work")


def test__replace_word__is_unchanged_when_replace_to_word_not_found_in_text():
    replace_word("It doesn't work", "work", 'car') == "It doesn't work"


def test__replace_word__is_unchanged_when_replace_from_word_not_found_in_text():
    replace_word("It doesn't work", "car", 'work') == "It doesn't work"




