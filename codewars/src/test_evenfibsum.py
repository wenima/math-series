"""Tests for https://www.codewars.com/kata/even-fibonacci-sum."""

import pytest


TEST = [
(0, 0),
(1, 0),
(33, 10),
(25997544, 19544084),
(10, 10),
(5, 2),
]


@pytest.mark.parametrize("n, result", TEST)
def test_eve_fib(n, result):
    """Test eve_fib returns correct fibonacci number."""
    from evenfibsum import eve_fib
    assert eve_fib(n) == result
