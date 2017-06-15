"""Solution for https://www.codewars.com/kata/fib-factorials/."""

from math import factorial

def sum_fib(n):
    """Return the sum of the factorials of the first n fibonacci numbers."""
    out = 0
    for x in range(n):
        out += factorial(fib(x))
    return out
    

def fib(n):
    """Return the nth fibonacci number."""
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a
