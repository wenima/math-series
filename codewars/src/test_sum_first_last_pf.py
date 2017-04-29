"""Tests for kata sum_first_last_pf."""

import pytest

TESTS_PF = [
    (70, [2, 5, 7]),
    (4, [2, 2]),
    (21, [3, 7]),
]


@pytest.mark.parametrize('n, result', TESTS_PF)
def test_prime_factors(n, result):
    """Test that the correct prime factors are returned."""
    from sum_first_last_pf import prime_factors
    assert prime_factors(n) == result
