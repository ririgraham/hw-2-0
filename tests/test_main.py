from src.divide import divide, calculate_logarithm, reverse_string
from scr.main import finder
import pytest


def test_divide():
    assert divide(2, 1) == 2

    assert divide(2, 0) == 0


def test_log():
    assert calculate_logarithm(8, 2) == 3.0

    with pytest.raises(ValueError):
        calculate_logarithm(0, 2)


@pytest.mark.parametrize('value, expected', [
    ('123', '321'),
    ('hello', 'olleh'),
    ('world', 'dlrow')
])
def test_reverse_string(value, expected):
    assert reverse_string(value) == expected


# def test_reverse_string_num(numbers):
#     assert reverse_string('123') == numbers
#
#
# def test_reverse_string(string):
#     assert reverse_string('hello') == string


def test_finder_basic():
    assert finder([1, '2', [], {}, ('3',)], int) == 1
