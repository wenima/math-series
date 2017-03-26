"""Tests for https://www.codewars.com/kata/steps-in-primes/python."""

import pytest


TEST = [
    (2,100,110, [101, 103]),
    (4,100,110, [103, 107]),
    (6,100,110, [101, 107]),
    (8,300,400, [359, 367]),
    (10,300,400, [307, 317]),
    (10, 100, 110, None),
    (4, 30000, 100000, [30109, 30113]),
    (2, 10000139, 10000141, [10000139, 10000141]),

]


@pytest.mark.parametrize('g, m, n, result', TEST)
def test_step(g, m, n, result):
    """Test step returns correct pair."""
    from step_primes import step
    assert step(g, m, n) == result
