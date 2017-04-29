"""Tests for kata k primes."""

import pytest

TESTS_PF = [
    (5, 500, 600, [500, 520, 552, 567, 588, 592, 594]),
    (5, 592, 600, [592, 594]),
    (2, 2, 20, [4, 6, 9, 10, 14, 15]),
    (20, 100, 200, []),
    (1, 2, 10, [2, 3, 5, 7]),
]

PUZZLE_PRIMES = [
    (138, {1: [2], 3: [8], 7: [128]}),
    (143, {1: [2, 3, 5, 7], 3: [8, 12], 7: [128]}),
]

PUZZLE_SOLUTIONS = [
    (138, 1),
    (143, 2),
    (1, 0)
]



@pytest.mark.parametrize('k, start, end, result', TESTS_PF)
def test_k_primes(k, start, end, result):
    """Test that the correct k primes within start and end are returned."""
    from k_primes import countKprimes
    assert countKprimes(k, start, end) == result

@pytest.mark.parametrize('n, result', PUZZLE_PRIMES)
def test_puzzle_pieces(n, result):
    """Test that the correct primes for puzzle are returned."""
    from k_primes import puzzle_pieces
    assert puzzle_pieces(n) == result

@pytest.mark.parametrize('n, result', PUZZLE_SOLUTIONS)
def test_puzzle(n, result):
    """Test that the correct number of solutions are returned."""
    from k_primes import puzzle
    assert puzzle(n) == result
