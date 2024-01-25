from functions.level_3.models import Expense, ExpenseCategory
from functions.level_3.four_fraud import find_fraud_expenses
from conftest import make_expenses



def test__find_fraud_expenses__if_get_fraud_chains():
    history = [
        make_expenses(amount = '100'),
        make_expenses(amount = '100'),
        make_expenses(amount = '100')
    ]

    expected_fraud_transactions = history
    assert  find_fraud_expenses(history) == expected_fraud_transactions


def test__find_fraud_expenses__if_get_no_fraud_expenses_with_amount_more_than_max_fraud_amount():
    history = [
        make_expenses(amount = '5000'),
        make_expenses(amount = '5001'),
        make_expenses(amount = '6000')
    ]

    expected_fraud_transactions = []
    assert  find_fraud_expenses(history) == expected_fraud_transactions


def test__find_fraud_expenses__if_get_no_fraud_expenses_with_small_number_of_chains():
    history = [
        make_expenses(amount = '1000'),
        make_expenses(amount = '1001'),
    ]

    expected_fraud_transactions = []
    assert  find_fraud_expenses(history) == expected_fraud_transactions

