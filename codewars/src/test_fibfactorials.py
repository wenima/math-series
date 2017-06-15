"""Tests for https://www.codewars.com/kata/fib-factorials/."""

import pytest


TEST = [
(2, 2),
(3, 3),
(4, 5),
(10, 295232799039604140898709551821456501251),
]


@pytest.mark.parametrize("n, result", TEST)
def test_sum_fib(n, result):
    """Test sum_fib returns correct fib factorial."""
    from fibfactorials import sum_fib
    assert sum_fib(n) == result
