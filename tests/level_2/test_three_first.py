from functions.level_2.three_first import first
import pytest

def test__first__if_items_and_not_default_found():
    assert first([1,2,3]) == 1


def test__first__if_items_and_default_found():
    assert first([1,2,3],5) == 1


def test__first__if_not_items_found_default_found():
    assert first([], 5) == 5


def test__first__if_not_items_found_default_is_NOT_SET():
    with pytest.raises(AttributeError):
        first([], 'NOT_SET')


def test__first__if_invalid_items_found():
    with pytest.raises(TypeError):
        first(1, 'NOT_SET')





