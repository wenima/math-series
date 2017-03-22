"""Tests for https://www.codewars.com/kata/find-fibonacci-last-digit."""
import pytest


TEST = [
    (193150, 5),
    (300, 0),
    (20001, 6),
    (800, 5),
    (1001, 1),
    (100, 5),
    (260, 5),
    (1111, 9),
    (1234, 7),
    (99999, 6),
    (10, 5),
    (234, 2),
    (193241, 1),
    (79, 1),
    (270, 0),
]


@pytest.mark.parametrize("n, result", TEST)
def test_fibonacci(n, result):
    """Test fibonacci for some value of n."""
    from find_fib_last_digit import get_last_digit
    assert get_last_digit(n) == result
