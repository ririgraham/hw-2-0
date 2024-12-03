import pytest
from src.masks import get_mask_account
from src.widget import mask_account_card, get_date
from src.utils import get_mask_card_number


#TESTS FOR MASKS.PY
@pytest.mark.parametrize(
    'card_number, expected_result',
    [
        ('7000792289606361', '7000 79** **** 6361'),
        ('1234567890123456', '1234 56** **** 3456'),
        (1234567812345678, '1234 56** **** 5678'),
        ('999', '999 ** **** 999'),
        ('12', '12 ** **** 12'),
        ('1122334455667881122334455667788', '1122 33** **** 7788'),
        ('', ' ** **** '),
    ]
)
def test_get_mask_card_number(card_number, expected_result):
    """Parametrized func to test card number masking"""
    assert get_mask_card_number(card_number) == expected_result


@pytest.mark.parametrize(
    'account_number, expected_result',
    [
        (7365410843105874305, '**4305'),
        ('987654321', '**4321'),
        (123, '**123'),
        (1, "**1"),
        ('', '**'),
    ]
)
def test_get_mask_account(account_number, expected_result):
    """Parametrized func to test account number masking"""
    assert get_mask_account(account_number) == expected_result


def test_get_mask_card_fixture(card_numbers):
    """Testing with fixtures"""
    for card_number, expected_result in card_numbers:
        assert get_mask_card_number(card_number) == expected_result


def test_get_mask_account_fixture(account_numbers):
    """Testing with fixtures"""
    for account_number, expected_result in account_numbers:
        assert get_mask_account(account_number) == expected_result


#TESTS FOR WIDGET.PY
@pytest.mark.parametrize('input_data, expected', [
    ('Visa 7000792289606378', 'Visa 7000 79** **** 6378'),
    ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('Счет 73654108430135874305', 'Счет **4305'),
    ('Счет 64686473678894779589', 'Счет **9589'),
])
def test_mask_account_card_valid(input_data, expected):
    '''Parametrized testind of masking card/account'''
    assert mask_account_card(input_data) == expected

def test_mask_account_card_invalid(invalid_inputs):
    '''Parametrized testing of invalid data'''
    for input_data in invalid_inputs:
        assert mask_account_card(input_data) == 'Incorrect Input'


def test_mask_account_fixture(valid_account_data):
    """Fixture test for card and account data"""
    for data, expected_result in valid_account_data:
        assert mask_account_card(data) == expected_result


@pytest.mark.parametrize('input_date, expected', [
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('2000-01-01T00:00:00.681256', '01.01.2000'),
    ('1999-12-31T23:59:59.621101', '31.12.1999'),
])
def test_get_date_valid(input_date, expected):
    '''Parametrized testing of valid date'''
    assert get_date(input_date) == expected

def test_get_date_invalid(invalid_date_input):
    '''Parametrized testing of invalid date'''
    for input_date in invalid_date_input:
        with pytest.raises(ValueError):
            get_date(input_date)


def test_get_date_fixture(date_test_valid):
    """Fixture testing date data"""
    for date_str, expected_result in date_test_valid:
        assert get_date(date_str) == expected_result
