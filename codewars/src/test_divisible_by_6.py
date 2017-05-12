"""Tests for https://www.codewars.com/kata/simple-fun-number-258-is-divisible-by-6."""

import pytest


TEST = [
("1*0",["120","150","180"]),
("*2",["12", "42", "72"]),
("*",["6"]),
("*1",[]),
("*2",["12", "42", "72"]),
("81234567890*",["812345678904"]),
("41*",["414"]),
("2345*345729",[]),
("*6",["6", "36", "66", "96"]),
("2345*345729",[]),
("1234567890123456789012345678*0",["123456789012345678901234567800",
"123456789012345678901234567830", "123456789012345678901234567860",
"123456789012345678901234567890"]),
]


@pytest.mark.parametrize("s, result", TEST)
def test_is_divisible_by_6(s, result):
    """Test function returns expected result."""
    from divisible_by_6 import is_divisible_by_6
    assert is_divisible_by_6(s) == result
