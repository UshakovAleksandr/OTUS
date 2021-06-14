from homework_01.main import *
import pytest


@pytest.mark.parametrize("test_input, expected", [([1, 2, 3, 4], [1, 4, 9, 16]),
                                                  ([2, 4, 45, 54], [4, 16, 2025, 2916]),
                                                  ([4, 43, 23, 57], [16, 1849, 529, 3249])]
                         )
def test_power_numbers(test_input, expected):
    assert power_numbers(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [([1, 2, 3, 4, 5, 6, 7], [1, 3, 5, 7])])
def test_filter_numbers_odd(test_input, expected):
    ODD = "odd"
    assert filter_numbers(test_input, ODD) == expected


@pytest.mark.parametrize("test_input, expected", [([1, 2, 3, 4, 5, 6, 7], [2, 4, 6])])
def test_filter_numbers_even(test_input, expected):
    EVEN = "even"
    assert filter_numbers(test_input, EVEN) == expected


@pytest.mark.parametrize("test_input, expected", [([1, 2, 4, 5, 7, 11, 14, 23, 30, 34, 45, 56],
                                                   [1, 2, 5, 7, 11, 23])])
def test_filter_numbers_prime(test_input, expected):
    PRIME = "prime"
    assert filter_numbers(test_input, PRIME) == expected


@pytest.mark.parametrize("test_input, expected", [([1, 2, 4, 5, 7, 11, 14, 23, 30, 34, 45, 56],
                                                   [1, 2, 5, 7, 11, 23])])
def test_is_prime(test_input, expected):
    assert is_prime(test_input) == expected
