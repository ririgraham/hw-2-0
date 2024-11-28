import pytest
from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date

#FIXTURES FOR MASKS.PY
@pytest.fixture
def card_numbers():
    """Fixtures for input card data"""
    return [
        ('700079228906361', '7000 79** **** 6361'),
        ('1234567890123456', '1234 56** **** 3456'),
        (1234567812345678, '1234 56** **** 5678'),
        ('999', '999 ** **** 999')
    ]


@pytest.fixture
def account_numbers():
    """Fixtures for input account data"""
    return [
        (7365410843105874305, '**4305'),
        ('987654321', '**4321'),
        (123, '**123'),
    ]


#FIXTURES FOR WIDGET.PY
@pytest.fixture
def account_card_data():
    """Fixture for correct card and account input"""
    return [
        ('Visa Platinum 700079228906361', 'Visa 7000 79** **** 6361'),
        ('Счет 7365410843105874305', 'Счет **4305'),
    ]


@pytest.fixture
def date_test_data():
    """Fixture for correct date input"""
    return [
        #correct dates
        ('2024-03-11T12:26:18.671407', '11.03.2024'),
        ('2000-01-01T00:00:00', '01.01.2000'),
        ('1999-12-31T23:59:59', '31.12.1999'),

        #incorrect dates
        ('2024-03-11', None),
        ('Invalid Date', None),
        ('', None)
    ]
