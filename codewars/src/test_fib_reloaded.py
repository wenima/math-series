"""Tests for https://www.codewars.com/kata/fibonacci-reloaded-sum."""

import pytest


TEST = [
(1, 0),
(3, 1),
(21, 6765),
(51, 12586269025),
(100, 218922995834555169026),
(200, 173402521172797813159685037284371942044301),
]


@pytest.mark.parametrize("n, result", TEST)
def test_fib(n, result):
    """Test nth_fib returns correct fibonacci number."""
    from fib_reloaded import fib
    assert fib(n) == result

@pytest.mark.parametrize("n, result", TEST)
def test_fib_functools(n, result):
    """Test nth_fib returns correct fibonacci number."""
    from fib_reloaded import fib_functools
    assert fib_functools(n) == result
