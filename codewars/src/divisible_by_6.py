"""This module solves kata https://www.codewars.com/kata/simple-fun-number-258-is-divisible-by-6."""

from math import sqrt

def is_divisible_by_6(s):
    """Return a list of all numbers divisible by 6 given input string and asterisk
    replaced by a digit."""
    if int(s[-1]) % 2:
        return []
    num = [c for c in s]
    idx = num.index('*')
    out = []
    for n in range(10):
        num[idx] = str(n)
        if sum([int(x) for x in num]) % 3 == 0:
            out.append(''.join(num))
    return out
