"""Tests for series function."""
import pytest


FIBONACCI_NUMBERS = [
    [0, 0],
    [1, 1],
    [2, 1],
    [3, 2],
    [4, 3],
    [5, 5],
    [6, 8],
    [7, 13],
    [8, 21],
    [9, 34],
    [10, 55],
    [30, 832040],
]


LUCAS_NUMBERS = [
    [0, 2],
    [1, 1],
    [2, 3],
    [3, 4],
    [4, 7],
    [5, 11],
    [6, 18],
    [7, 29],
    [8, 47],
    [9, 76],
    [10, 123],
    [30, 1860498],
]


WILSON_NUMBERS = [
    [6, 5, 2, 41],
    [4, 6, 9, 39],
    [5, 4, 2, 22],
    [7, 3, 10, 154],
]


@pytest.mark.parametrize("n, result", FIBONACCI_NUMBERS)
def test_fibonacci(n, result):
    """Test fibonacci for some value of n."""
    from series import fibonacci
    assert fibonacci(n) == result


def test_fibonacci_exists():
    """Test whether fibonacci function exists."""
    import series
    assert series.fibonacci


def test_fib_0():
    """Test output of fibanacci with argument 0."""
    from series import fibonacci
    assert fibonacci(0) == 0


def test_lucas_exists():
    """Test whether lucas function exists."""
    import series
    assert series.lucas


def test_lucas_0():
    """Test output of lucas with argument 0."""
    from series import lucas
    assert lucas(0) == 2


@pytest.mark.parametrize("n, result", LUCAS_NUMBERS)
def test_lucas(n, result):
    """Test lucas for some value of n."""
    from series import lucas
    assert lucas(n) == result


def test_sum_series_exists():
    """Test whether the sum_series function exists."""
    import series
    assert series.sum_series


def test_sum_series_0_default():
    """Test sum_series(0) with default values."""
    from series import sum_series
    assert sum_series(0) == 0


@pytest.mark.parametrize("n, result", FIBONACCI_NUMBERS)
def test_sum_series_default(n, result):
    """Test sum_series for some value of n with default values."""
    from series import sum_series
    assert sum_series(n) == result


@pytest.mark.parametrize("n, result", LUCAS_NUMBERS)
def test_sum_series_lucas(n, result):
    """Test sum_series to return lucas numbers."""
    from series import sum_series
    assert sum_series(n, 2, 1) == result


@pytest.mark.parametrize("n, a, b, result", WILSON_NUMBERS)
def test_sum_series_wilson(n, a, b, result):
    """Test sum_series to return another series' numbers."""
    from series import sum_series
    assert sum_series(n, a, b) == result
