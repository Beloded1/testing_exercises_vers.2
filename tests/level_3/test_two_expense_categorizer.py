from functions.level_3.two_expense_categorizer import guess_expense_category
from functions.level_3.models import ExpenseCategory
from conftest import make_expenses
import pytest


@pytest.mark.parametrize(
    'expence, ExpenseCategory',
    [
        (make_expenses(spent_in='Bastard place'),
        ExpenseCategory.BAR_RESTAURANT),
        (make_expenses(spent_in='nice clean house'),
        ExpenseCategory.SUPERMARKET),
        (make_expenses(spent_in='Netflix USA'),
        ExpenseCategory.ONLINE_SUBSCRIPTIONS),
        (make_expenses(spent_in='Wonder pharm'),
        ExpenseCategory.MEDICINE_PHARMACY),]
)
def test__guess_expence_category__if_spent_in_contains_trigger_words(expence, ExpenseCategory):
    assert guess_expense_category(expence) == ExpenseCategory


@pytest.mark.parametrize(
    'expense, ExpenseCategory',
    [
        (make_expenses(spent_in='Bastard'),
        ExpenseCategory.BAR_RESTAURANT),
        (make_expenses(spent_in='pharm'),
        ExpenseCategory.MEDICINE_PHARMACY),
        (make_expenses(spent_in='www.taxi.yandex.ru'),
        ExpenseCategory.TRANSPORT),

    ]
)
def test__guess_expense_category__if_spent_in_is_trigger_word(expense, ExpenseCategory):
    assert guess_expense_category(expense) == ExpenseCategory


def test__guess_expence_category__if_spent_in_does_not_have_trigger_words():
    expense = make_expenses(spent_in= "Y Ivana")
    assert guess_expense_category(expense) == None


def test__guess_expence_category__if_spent_in_is_not_valid():
    expense = make_expenses(spent_in= 123)
    with pytest.raises(AttributeError):
        guess_expense_category(expense)
