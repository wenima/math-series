"""Tests for kata primes_in_number."""

import pytest

TESTS_PF = [
    (1, []),
    (70, [2, 5, 7]),
    (4, [2, 2]),
    (10, [2, 5]),
    (8, [2, 2, 2]),
    (3, [3]),
    (12, [2, 2, 3]),
]

TESTS_HIGHEST = [
    (2, 3, 50, [48, 4, 1]),
    (5, 11, 1000, [605, 1, 2]),
    (3, 13, 5000, [4563, 3, 2]),
    (5, 7, 5000, [4375, 4, 1]),
]



@pytest.mark.parametrize('n, result', TESTS_PF)
def test_prime_factors(n, result):
    """Test that the correct prime factors are returned."""
    from highest_bi_prime import prime_factors
    assert prime_factors(n) == result


@pytest.mark.parametrize('p1, p2, end, result', TESTS_HIGHEST)
def test_highest_biPrimefac(p1, p2, end, result):
    """Test that the correct result are returned."""
    from highest_bi_prime import highest_biPrimefac
    assert highest_biPrimefac(p1, p2, end) == result
