"""Tests for kata k primes."""

import pytest

TESTS_PF = [
    (5, 500, 600, [500, 520, 552, 567, 588, 592, 594]),
    (5, 592, 600, [592, 594]),
    (2, 2, 20, [4, 6, 9, 10, 14, 15]),
    (20, 100, 200, []),
]



@pytest.mark.parametrize('k, start, end, result', TESTS_PF)
def test_k_primes(k, start, end, result):
    """Test that the correct k primes within start and end are returned."""
    from k_primes import countKprimes
    assert countKprimes(k, start, end) == result
