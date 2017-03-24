"""This module solves kata https://www.codewars.com/kata/n-th-fibonacci."""

def original_solution(n):
    """Return the nth fibonacci number."""
    if n == 1:
        return 0
    a, b = 0, 1
    for i in range(1, n - 1):
        a, b = b, (a + b)
    return b

#better solution
def nth_fib(n):
    """Return the nth fibonacci number. Per the kata, f(1) is supposed to be
    0 so the fibonacci sequence for this kata was not indexed at 0."""
    a, b = 0, 1
    for __ in range(n-1):
        a, b = b, a + b
    return a
