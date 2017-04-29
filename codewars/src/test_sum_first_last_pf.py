"""Tests for kata sum_first_last_pf."""

import pytest

TESTS_PF = [
    (70, [2, 5, 7]),
    (4, [2, 2]),
    (21, [3, 7]),
]


SLPF = [
    (10, 100, [21, 25, 63]),
    (10, 200, [21, 25, 63, 105, 125, 147, 189]),
    (15, 150, [26, 52, 78, 104, 130]),
    (501, 1000, [998]),
    (501, 5000, [998, 1996, 2994, 3992, 4990]),
]


@pytest.mark.parametrize('n, result', TESTS_PF)
def test_prime_factors(n, result):
    """Test that the correct prime factors are returned."""
    from sum_first_last_pf import prime_factors
    assert prime_factors(n) == result


@pytest.mark.parametrize('val, end, result', SLPF)
def test_sflpf_data(val, end, result):
    """Test that the correct value is returned."""
    from sum_first_last_pf import sflpf_data
    assert sflpf_data(val, end) == result
