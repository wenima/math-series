"""Tests for https://www.codewars.com/kata/goldbachs-conjecture-prime-numbers."""

import pytest


TEST = [
    (6, [[3, 3]]),
    (8, [[3, 5]]),
    (10, [[3, 7], [5, 5]]),
    (18, [[5, 13], [7, 11]]),
    (34, [[3, 31], [5, 29], [11, 23], [17, 17]]),
]


@pytest.mark.parametrize("n, result", TEST)
def test_goldbach(n, result):
    """Test that goldbach returns correct pairs of primes."""
    from goldbach import goldbach
    assert goldbach(n) == result
