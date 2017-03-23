"""Tests for https://www.codewars.com/kata/find-fibonacci-last-digit."""

import pytest


TEST = [
(1, 1),
(21, 6),
(302, 1),
(4003, 7),
(50004, 8),
(600005, 5),
(7000006, 3),
(80000007, 8),
(900000008, 1),
(1000000009, 9),
]


@pytest.mark.parametrize("n, result", TEST)
def test_last_fib_digit(n, result):
    """Test last digit for nth fibonacci number."""
    from last_fib_digit import last_fib_digit
    assert last_fib_digit(n) == result
