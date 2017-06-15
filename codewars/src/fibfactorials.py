"""Solution for https://www.codewars.com/kata/fib-factorials/."""

from math import factorial as fac

def sum_fib(n):
    """Return the sum of the factorials of the first n fibonacci numbers."""
    return sum(fac(fib(x)) for x in range(n))

def fib(n):
    """Return the nth fibonacci number."""
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


"""nicer solution"""
from math import factorial as fac

def sum_fib_nicer(n):
    a, b, s = 0, 1, 0
    while n:
        s += fac(a)
        a, b = b, a+b
        n -= 1
    return s
