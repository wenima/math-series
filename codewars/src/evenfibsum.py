"""This module solves kata https://www.codewars.com/kata/even-fibonacci-sum."""

from bisect import bisect_left
from math import sqrt

def get_first_100_fibs():
    """Return a list with the first 100 fib numbers."""
    return [int(((sqrt(5) + 1) / 2) ** n / sqrt(5) + 0.5) for n in range(100)]

def binary_search(a, x, lo=0, hi=None):
  """Return the nearest index of value x from iterable a."""
  hi = hi if hi is not None else len(a)
  pos = bisect_left(a,x,lo,hi)
  return pos

def eve_fib(n):
    """Return the sum of all even fibonacci numbers up to but not including, n."""
    first_100_fibs = get_first_100_fibs()
    return sum([n for n in first_100_fibs[:binary_search(first_100_fibs, n)] if n % 2 == 0])
