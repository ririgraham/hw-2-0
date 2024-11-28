import pytest
from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date

#TESTS FOR MASKS.PY
@pytest.mark.parametrize(
    'card_number, expected_result',
    [
        ('700079228906361', '7000 79** **** 6361'),
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
@pytest.mark.parametrize(
    'data, expected_result',
    [
        #testing card numbers
        ('Visa Platinum 700079228906361', 'Visa 7000 79** **** 6361'),
        ('MasterCard 715830073426758', 'MasterCard 7158 30** **** 6758'),
        ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),

        #testing account numbers
        ('Счет 7365410843105874305', 'Счет **4305'),
        ('Счет 64684673687894779589', 'Счет **9589'),

        #testing incorrect data
        ('Invalid Input', 'Incorrect Input'),
        ('12345', 'Incorrect Input'),
        ('', 'Incorrect Input'),
    ]
)
def test_mask_account_card(data, expected_result):
    """Parametrized test for card and account data"""
    assert mask_account_card(data) == expected_result


def test_mask_account_card_fixture(account_card_data):
    """Fixture test for card and account data"""
    for data, expected_result in account_card_data:
        assert mask_account_card(data) == expected_result


@pytest.mark.parametrize(
    'date_str, expected_result',
    [
        #correct date
        ('2024-03-11T12:26:18.671407', '11.03.2024'),
        ('2000-01-01T00:00:00', '01.01.2000'),
        ('1999-12-31T23:59:59', '31.12.1999'),

        #incorrect dates
        ('2024-03-11', None),
        ('Invalid Date', None),
        ('', None),
    ]
)
def test_get_date(date_str, expected_result):
    """Parametrized testing date data"""
    assert get_date(date_str) == expected_result


def test_get_date_fixture(date_test_data):
    """Fixture testing date data"""
    for date_str, expected_result in date_test_data:
        if expected_result is None:
            with pytest.raises(ValueError):
                get_date(date_str)
        else:
            assert get_date(date_str) == expected_result
