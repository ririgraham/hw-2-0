from typing import Union

import pytest


# FIXTURES FOR MASKS.PY
@pytest.fixture
def card_numbers() -> list:
    """Fixtures for input card data"""
    return [
        ("700079228906361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456"),
        (1234567812345678, "1234 56** **** 5678"),
        ("999", "999 ** **** 999"),
    ]


@pytest.fixture
def account_numbers() -> list:
    """Fixtures for input account data"""
    return [
        (7365410843105874305, "**4305"),
        ("987654321", "**4321"),
        (123, "**123"),
    ]


# FIXTURES FOR WIDGET.PY
@pytest.fixture
def valid_card_data() -> list:
    """Fixture for correct card inputs"""
    return [
        ("Visa 7000792289606378", "Visa 7000 79** **** 6378"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ]


@pytest.fixture
def valid_account_data() -> list:
    """Fixture for correct account inputs"""
    return [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 64686473678894779589", "Счет **9589"),
    ]


@pytest.fixture
def invalid_inputs() -> list:
    """Fixture for invalid data"""
    return [
        "InvalidData159",
        "",
        "Card4343",
        "Счет 828",
    ]


@pytest.fixture
def date_test_valid() -> list:
    """Fixture for correct date input"""
    return [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2000-01-01T00:00:00.681256", "01.01.2000"),
        ("1999-12-31T23:59:59.621101", "31.12.1999"),
    ]


@pytest.fixture
def invalid_date_input() -> list:
    """Fixture for incorrect date inputs"""
    return [
        "",
        "InvalidDate",
        "2024-04-16",
    ]


# FIXTURES FOR PROCESSING.PY
@pytest.fixture
def sample_data() -> list:
    """Fixture for test data"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
