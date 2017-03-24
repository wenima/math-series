"""Tests for https://www.codewars.com/kata/even-fibonacci-sum."""

import pytest


TEST = [
(0, 0),
(1, 0),
(33, 10),
(25997544, 19544084),
(10, 10),
(5, 2),
]


@pytest.mark.parametrize("n, result", TEST)
def test_even_fib(n, result):
    """Test eve_fib returns correct fibonacci number."""
    from evenfibsum import even_fib
    assert even_fib(n) == result


@pytest.mark.parametrize("n, result", TEST)
def test_even_fib_concise(n, result):
    """Test eve_fib returns correct fibonacci number."""
    from evenfibsum import even_fib_concise
    assert even_fib_concise(n) == result


@pytest.mark.parametrize("n, result", TEST)
def test_even_fib_clever(n, result):
    """Test eve_fib returns correct fibonacci number."""
    from evenfibsum import even_fib_clever
    assert even_fib_clever(n) == result


@pytest.mark.parametrize("n, result", TEST)
def test_even_fib_g(n, result):
    """Test eve_fib returns correct fibonacci number."""
    from evenfibsum import even_fib_g
    assert even_fib_g(n) == result
