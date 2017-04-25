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



@pytest.mark.parametrize('n, result', TESTS_PF)
def test_prime_factors(n, result):
    """Test that the correct prime factors are returned."""
    from prime_factors import prime_factors
    assert prime_factors(n) == result
