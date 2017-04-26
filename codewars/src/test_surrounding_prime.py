"""Tests for https://www.codewars.com/kata/steps-in-primes/python."""

import pytest


TEST = [
    (100, [97, 101]),
    (97, [89, 101]),
    (101, [97, 103]),
    (120, [113, 127]),
    (130, [127, 131]),
]


@pytest.mark.parametrize('p, result', TEST)
def test_before_after(p, result):
    """Test before_after returns correct pair."""
    from surrounding_prime import prime_bef_aft
    assert prime_bef_aft(p) == result
