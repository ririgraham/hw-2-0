from typing import Union

import pytest

from src.masks import get_mask_account
from src.processing import filter_by_state, sort_by_date
from src.utils import get_mask_card_number
from src.widget import get_date, mask_account_card


# TESTS FOR MASKS.PY
@pytest.mark.parametrize(
    "card_number, expected_result",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456"),
        (1234567812345678, "1234 56** **** 5678"),
        ("999", "999 ** **** 999"),
        ("12", "12 ** **** 12"),
        ("1122334455667881122334455667788", "1122 33** **** 7788"),
        ("", " ** **** "),
    ],
)
def test_get_mask_card_number(card_number: Union[str, int], expected_result: Union[str, int]) -> None:
    """Parametrized func to test card number masking"""
    assert get_mask_card_number(card_number) == expected_result


@pytest.mark.parametrize(
    "account_number, expected_result",
    [
        (7365410843105874305, "**4305"),
        ("987654321", "**4321"),
        (123, "**123"),
        (1, "**1"),
        ("", "**"),
    ],
)
def test_get_mask_account(account_number: Union[str, int], expected_result: Union[str, int]) -> None:
    """Parametrized func to test account number masking"""
    assert get_mask_account(account_number) == expected_result


def test_get_mask_card_fixture(card_numbers: list) -> None:
    """Testing with fixtures"""
    for card_number, expected_result in card_numbers:
        assert get_mask_card_number(card_number) == expected_result


def test_get_mask_account_fixture(account_numbers: list) -> None:
    """Testing with fixtures"""
    for account_number, expected_result in account_numbers:
        assert get_mask_account(account_number) == expected_result


# TESTS FOR WIDGET.PY
@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Visa 7000792289606378", "Visa 7000 79** **** 6378"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 64686473678894779589", "Счет **9589"),
    ],
)
def test_mask_account_card_valid(input_data: str, expected: str) -> None:
    """Parametrized testind of masking card/account"""
    assert mask_account_card(input_data) == expected


def test_mask_account_card_invalid(invalid_inputs: list) -> None:
    """Parametrized testing of invalid data"""
    for input_data in invalid_inputs:
        assert mask_account_card(input_data) == "Incorrect Input"


def test_mask_account_fixture(valid_account_data: list) -> None:
    """Fixture test for card and account data"""
    for data, expected_result in valid_account_data:
        assert mask_account_card(data) == expected_result


@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2000-01-01T00:00:00.681256", "01.01.2000"),
        ("1999-12-31T23:59:59.621101", "31.12.1999"),
    ],
)
def test_get_date_valid(input_date: str, expected: str) -> None:
    """Parametrized testing of valid date"""
    assert get_date(input_date) == expected


def test_get_date_invalid(invalid_date_input: list) -> None:
    """Parametrized testing of invalid date"""
    for input_date in invalid_date_input:
        with pytest.raises(ValueError):
            get_date(input_date)


def test_get_date_fixture(date_test_valid: list) -> None:
    """Fixture testing date data"""
    for date_str, expected_result in date_test_valid:
        assert get_date(date_str) == expected_result


# TESTS FOR PROCESSING.PY
@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_filter_by_state(sample_data: list, state: str, expected: list) -> None:
    """testing state filtering"""
    result = filter_by_state(sample_data, state)
    assert result == expected


@pytest.mark.parametrize(
    "descending, expected",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(sample_data: list, descending: bool, expected: list) -> None:
    """testing date descendence"""
    result = sort_by_date(sample_data, descending=descending)
    assert result == expected
