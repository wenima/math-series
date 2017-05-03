"""Tests for kata k primes."""

import pytest

TESTS_PF = [
    (5, 500, 600, [500, 520, 552, 567, 588, 592, 594]),
    (5, 592, 600, [592, 594]),
    (2, 2, 20, [4, 6, 9, 10, 14, 15]),
    (20, 100, 200, []),
    (1, 2, 10, [2, 3, 5, 7]),
    (8, 10000000, 10000200, [10000096, 10000152, 10000165, 10000200]),
    (5, 1000, 1100, [1020, 1026, 1032, 1044, 1050, 1053, 1064, 1072, 1092, 1100]),
]

PUZZLE_PRIMES = [
    (138, {1: [2], 3: [8], 7: [128]}),
    (143, {1: [2, 3, 5, 7], 3: [8, 12], 7: [128]}),
    (250, {1: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
                67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113],
            3: [8, 12, 18, 20, 27, 28, 30, 42, 44, 45, 50, 52, 63, 66, 68, 70,
                75, 76, 78, 92, 98, 99, 102, 105, 110, 114, 116, 117],
            7: [128, 192]}),
]

PUZZLE_SOLUTIONS = [
    (138, 1),
    (143, 2),
    (1, 0),
    (659, 153),
]



@pytest.mark.parametrize('k, start, end, result', TESTS_PF)
def test_k_primes(k, start, end, result):
    """Test that the correct k primes within start and end are returned."""
    from k_primes import count_Kprimes
    assert count_Kprimes(k, start, end) == result

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
