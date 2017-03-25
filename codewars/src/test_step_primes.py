"""Tests for https://www.codewars.com/kata/calculate-fibonacci-return-count-of-digit-occurrences."""

import pytest


TEST = [
    (2,100,110), [101, 103]),
    (4,100,110), [103, 107]),
    (6,100,110), [101, 107]),
    (8,300,400), [359, 367]),
    (10,300,400), [307, 317]),

]


@pytest.mark.parametrize('g, m, n, result', TEST)
def test_step(g, m, n, result):
    """Test step returns correct pair."""
    from step_primes import step
    assert step(g, m, n) == result
