"""Tests for kata https://www.codewars.com/kata/multiples-of-3-and-5."""

import pytest

TESTS = [
    (10, 23),
]

@pytest.mark.parametrize('n, result', TEST)
def test_solution(n, result):
    """Test that the correct sum of multiples is returned."""
    from sum_of_multiples import solution
    assert solution(n) == result
