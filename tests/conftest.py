import pytest
from src.masks import get_mask_account
from src.widget import mask_account_card, get_date
from src.utils import get_mask_card_number


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
def valid_card_data():
    """Fixture for correct card inputs"""
    return [
        ('Visa 7000792289606378', 'Visa 7000 79** **** 6378'),
        ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
        ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ]
@pytest.fixture
def valid_account_data():
    '''Fixture for correct account inputs'''
    return [
        ('Счет 73654108430135874305', 'Счет **4305'),
        ('Счет 64686473678894779589', 'Счет **9589'),
    ]
@pytest.fixture
def invalid_inputs():
    '''Fixture for invalid data'''
    return [
        'InvalidData159',
        '',
        'Card4343',
        'Счет 828',
    ]
@pytest.fixture
def date_test_valid():
    """Fixture for correct date input"""
    return [
        ('2024-03-11T02:26:18.671407', '11.03.2024'),
        ('2000-01-01T00:00:00.681256', '01.01.2000'),
        ('1999-12-31T23:59:59.621101', '31.12.1999'),
    ]
@pytest.fixture
def invalid_date_input():
    '''Fixture for incorrect date inputs'''
    return [
        '',
        'InvalidDate',
        '2024-04-16',
    ]
