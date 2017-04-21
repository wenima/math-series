"""Tests for kata primes_in_number."""

import pytest

TESTS_PF = [
    (70, [2, 5, 7]),
    (4, [2, 2]),
]

TESTS_COMPOSITES = [
    (10, 100, [16, 27, 30, 60, 70, 72, 84]),
    (80, 150, [84, 105, 150]),
    (5076, 6259, [
                    5100, 5184, 5292, 5304, 5336, 5355, 5360, 5400, 5440, 5445,
                    5487, 5586, 5658, 5808, 5824, 5832, 5880, 5967, 6068, 6075,
                    6076, 6084, 6120, 6248
                ])
]


@pytest.mark.parametrize('n, result', TESTS_PF)
def test_prime_factors(n, result):
    """Test that the correct prime factors are returned."""
    from sum_of_prime_factors import prime_factors
    assert prime_factors(n) == result

@pytest.mark.parametrize('start, stop, result', TESTS_COMPOSITES)
def test_mul_primefactor_sum(start, stop, result):
    """Test that only non_prime_numbers are returned which can be divided by
    the sum of it's prime factors given a range."""
    from sum_of_prime_factors import mult_primefactor_sum
    assert mult_primefactor_sum(start, stop) == result
