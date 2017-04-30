"""Tests for https://www.codewars.com/kata/largest-prime-number-containing-n-digit/."""

import pytest


TEST = [
    (1, 7),
    (2, 97),
    (3, 997),
]


@pytest.mark.parametrize("n, result", TEST)
def test_largest(n, result):
    """Test that largest returns largest number with n digits."""
    from largest import largest
    assert largest(n) == result
