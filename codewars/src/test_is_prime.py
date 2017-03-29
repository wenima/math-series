"""Tests for https://www.codewars.com/kata/is-a-number-prime/discuss/python."""

import pytest


TEST = [
    (0, False),
    (1, False),
    (2, True),
]


@pytest.mark.parametrize("n, result", TEST)
def test_is_prime(n, result):
    """Test that is_prime returns True if given number is a prime."""
    from is_prime import is_prime
    assert is_prime(n) == result
