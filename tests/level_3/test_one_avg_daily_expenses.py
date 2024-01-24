from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses
from conftest import make_expenses
import pytest
import datetime
import decimal


def test__calculate_average_daily_expenses__if_expenses_occured_in_different_days():
    expenses = [
        make_expenses(
            amount='100.00',
            spent_at=datetime.datetime(2024, 1, 1, 0, 0, 0)
        ),
        make_expenses(
            amount='200.00',
            spent_at=datetime.datetime(2024, 1, 2, 0, 0, 0)
        ),
        make_expenses(
            amount='300.00',
            spent_at=datetime.datetime(2024, 1, 3, 0, 0, 0)
        ),
        make_expenses(
            amount='400.00',
            spent_at=datetime.datetime(2024, 1, 4, 0, 0, 0)
        ),
    ]
    expected_result = decimal.Decimal('250.00')
    assert calculate_average_daily_expenses(expenses) == expected_result


def test__calculate_average_daily_expenses__if_expense_occured_once_in_one_day():
    expenses = [
        make_expenses(
            amount='100.00',
            spent_at=datetime.datetime(2024, 1, 1, 0, 0, 0)
        ),
    ]
    expected_result = decimal.Decimal('100.00')
    assert calculate_average_daily_expenses(expenses) == expected_result


def test__calculate_average_daily_expenses__if_expenses_occured_in_one_day():
    expenses = [
        make_expenses(
            amount='100.00',
            spent_at=datetime.datetime(2024, 1, 1, 0, 0, 0)
        ),
        make_expenses(
            amount='100.00',
            spent_at=datetime.datetime(2024, 1, 1, 0, 0, 0)
        ),
        make_expenses(
            amount='100.00',
            spent_at=datetime.datetime(2024, 1, 1, 0, 0, 0)
        ),
        make_expenses(
            amount='500.00',
            spent_at=datetime.datetime(2024, 1, 1, 0, 0, 0)
        ),
    ]
    expected_result = decimal.Decimal('800.00')
    assert calculate_average_daily_expenses(expenses) == expected_result

def test__calculate_average_daily_expenses__if_wrong_input():
    with pytest.raises(TypeError):
        calculate_average_daily_expenses(1)

