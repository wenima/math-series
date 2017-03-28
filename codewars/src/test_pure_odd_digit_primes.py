"""Tests for https://www.codewars.com/kata/pure-odd-digits-primes."""

import pytest


TEST = [
    (20, [7, 19, 31]),
    (40, [9, 37, 53]),
]


@pytest.mark.parametrize('n, result', TEST)
def test_only_odd_digit_primes(n, result):
    """Test only_oddDigPrimes returns correct number of pure digit primes, largest pure digit prime
    smaller than n and next pure digit prime after n."""
    from pure-odd-digits-primes import only_oddDigPrimes
    assert only_oddDigPrimes(n) == result
