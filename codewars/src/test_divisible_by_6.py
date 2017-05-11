"""Tests for https://www.codewars.com/kata/simple-fun-number-258-is-divisible-by-6."""

import pytest


TEST = [
("1*0",["120","150","180"]),
("*2",["12", "42", "72"]),
]


@pytest.mark.parametrize("s, result", TEST)
def test_is_divisible_by_6(s, result):
    """Test last digit for nth fibonacci number."""
    from divisible_by_6 import is_divisible_by_6
    assert is_divisible_by_6(s) == result
