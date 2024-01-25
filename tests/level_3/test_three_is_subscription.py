from functions.level_3.three_is_subscription import is_subscription
from functions.level_3.models import ExpenseCategory
from conftest import make_expenses
import pytest
import datetime


def test__is_subscription__if_spent_in_the_same_place_at_different_months():
    expense = make_expenses(
            spent_in="Bar",
            spent_at=datetime.datetime(2024, 1, 1, 0, 0, 0))
    history = [
        make_expenses(
            spent_in="Bar",
            spent_at=datetime.datetime(2024, 2, 1, 0, 0, 0)
        ),
        make_expenses(
            spent_in="Bar",
            spent_at=datetime.datetime(2024, 3, 1, 0, 0, 0)
        ),
        make_expenses(
            spent_in="Bar",
            spent_at=datetime.datetime(2024, 1, 4, 0, 0, 0)
        ),
    ]
    assert is_subscription(expense, history) == True


def test__is_subscription__if_spent_in_the_same_place_at_less_than_three_months():
    expense = make_expenses(
            spent_in="Bar",
            spent_at=datetime.datetime(2024, 1, 1, 0, 0, 0))
    history = [
        make_expenses(
            spent_in="Bar",
            spent_at=datetime.datetime(2024, 2, 1, 0, 0, 0)
        ),
    ]
    assert is_subscription(expense, history) == False


def test__is_subscription__if_spent_in_the_different_places():
    expense = make_expenses(
            spent_in="Bar",
            spent_at=datetime.datetime(2024, 1, 1, 0, 0, 0))
    history = [
        make_expenses(
            spent_in="NeBAr",
            spent_at=datetime.datetime(2024, 2, 1, 0, 0, 0)
        ),
        make_expenses(
            spent_in="Y Ashota",
            spent_at=datetime.datetime(2024, 3, 1, 0, 0, 0)
        ),
        make_expenses(
            spent_in="Apple",
            spent_at=datetime.datetime(2024, 1, 4, 0, 0, 0)
        ),
    ]
    assert is_subscription(expense, history) == False


def test__is_subscription__if_spent_in_the_same_place_many_times_during_one_month():
    expense = make_expenses(
            spent_in="Bar",
            spent_at=datetime.datetime(2024, 2, 1, 0, 0, 0))
    history = [
        make_expenses(
            spent_in="Bar",
            spent_at=datetime.datetime(2024, 2, 1, 0, 0, 0)
        ),
        make_expenses(
            spent_in="Bar",
            spent_at=datetime.datetime(2024, 2, 2, 0, 0, 0)
        ),
        make_expenses(
            spent_in="Bar",
            spent_at=datetime.datetime(2024, 1, 4, 0, 0, 0)
        ),
    ]
    assert is_subscription(expense, history) == False

