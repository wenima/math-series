"""This module solves kata https://www.codewars.com/kata/fibonacci-reloaded."""

import sys

sys.setrecursionlimit(2000)

memo = {0: 0, 1: 0, 2: 1}
def fib(n):
    """Return nth fibonacci number starting at fib(1) == 0 using memoization."""
    if n in memo:
        return memo[n]
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


#using lru_cache
import functools
@functools.lru_cache()
def fib_functools(n):
    """Return nth fibonacci number starting at fib(1) == 0 using functools
    decorator."""
    # incorrect fib, but the tests expect it
    if n == 0: return 1
    if n in [1, 2]:
        return n-1
    return fib(n - 1) + fib(n - 2)
