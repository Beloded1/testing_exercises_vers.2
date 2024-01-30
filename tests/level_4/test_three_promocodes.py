from functions.level_4.three_promocodes import generate_promocode
import pytest
from unittest.mock import patch


@pytest.mark.parametrize('promocode_len, expected_result', [
    (0, 0),
    (1, 1),
    (11, 11),
])
def test__generate_promocode__if_check_len_promocode(promocode_len, expected_result):
    promocode = generate_promocode(promocode_len)
    assert len(promocode) == expected_result


def test__generate_promocode__with_default_len_promocode():
    promocode = generate_promocode()
    assert len(promocode) == 8


def test__generate_promocode_is_uppercase():
    promocode = generate_promocode()
    assert promocode == promocode.upper()


@pytest.mark.parametrize('return_value, expected_result', [
    ('A', 'AAAAAAAA'),
    ('C', 'CCCCCCCC'),
])
def test__generate_promocode__with_mock_choice(return_value, expected_result):
    with patch('functions.level_4.three_promocodes.random.choice') as random_choice:
        random_choice.return_value = return_value
        promocode = generate_promocode()
        assert promocode == expected_result
        assert len(promocode) == 8
