"""This module solves kata https://www.codewars.com/kata/simple-fun-number-258-is-divisible-by-6."""


def is_divisible_by_6(s):
    """Return a list of all numbers divisible by 6 given input string and asterisk
    replaced by a digit."""
    if s == '*': return ['6']
    out = []
    num = [c for c in s]
    idx = num.index('*')
    for n in range(10):
        num[idx] = str(n)
        if int(num[-1]) % 2 == 0 and sum([int(x) for x in num]) % 3 == 0:
            out.append(''.join(num) if int(num[0]) else ''.join(num[1:]))
    return out
