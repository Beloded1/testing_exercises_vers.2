from functions.level_3.models import Expense, ExpenseCategory, Currency, BankCard
from functions.level_4.two_students import Student
import pytest
import decimal
import datetime
import os
import configparser


def make_expenses(
    amount: str = "100",
    currency = Currency.RUB,
    card = BankCard(last_digits="1234", owner="Alexandr"),
    spent_in = "Online Store",
    spent_at = datetime.datetime(2023, 1, 1, 0, 0, 0),
    category: ExpenseCategory | None = None
) -> Expense:
    return Expense(
        amount=decimal.Decimal(amount),
        currency=currency,
        card=card,
        spent_in=spent_in,
        spent_at=spent_at,
        category=category
    )


@pytest.fixture
def students() -> list[Student]:
    return [
        Student('John', 'Doe', '@johndoe'),
        Student('Jane', 'Doe', '@janedoe'),
        Student('Alice', 'Smith', None),
        Student('Bob', 'Johnson', '@bobjohnson'),
        Student('Charlie', 'Brown', '@charliebrown')
    ]


@pytest.fixture
def filepath(request):
    lines, expected_result = request.param
    path_to_file = 'test_file.txt'
    with open(path_to_file, 'w') as file:
        file.writelines([f'{line}\n' for line in lines])

    yield path_to_file, expected_result

    os.remove(path_to_file)


@pytest.fixture
def config_file_path(request):
    data, field_name, expected_result = request.param
    config = configparser.ConfigParser()
    path_to_file = 'config.ini'

    for section, section_data in data.items():
        config.add_section(section)
        for field, value in section_data.items():
            config.set(section, field, value)

    with open(path_to_file, 'w') as config_file:
        config.write(config_file)

    yield path_to_file, field_name, expected_result

    os.remove(path_to_file)
