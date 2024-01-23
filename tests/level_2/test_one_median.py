from functions.level_2.one_median import get_median_value
import pytest


def test__get_median_value__if_not_items_return_None():
    assert get_median_value([]) == None


@pytest.mark.xfail
def test__get_median_value__return_midle_index_if_even_len_of_items_found():
    assert get_median_value([2, 1, 4, 3]) == 1


@pytest.mark.xfail(reason='Incorrect calculation')
def test__get_median_value__return_middle_index_if_more_even_items_found():
    assert get_median_value([2, 1, 4, 3, 5, 6]) == 3


@pytest.mark.xfail(reason='Incorrect calculation')
def test__get_median_value__return_middle_index_if_odd_len_of_items_found():
    assert get_median_value([1, 3, 6, 8, 9]) == 6
