"""Module to solve the code-kata https://www.codewars.com/kata/steps-in-primes/python."""

from itertools import islice


def prime(a):
    """Return True if a is prime."""
    if a == 2: return True
    if a < 2 or a % 2 == 0: return False
    return not any(a % x == 0 for x in range(3, int(a**0.5) + 1, 2))


def step(g, m, n):
    """Return the first pair of primes between m and n with step g."""
    primes = [i for i in range(m, n) if prime(i)]
    try:
        return next([p, q] for idx, p in enumerate(primes, 1) for q in islice(primes, idx, len(primes)) if q - p == g)
    except StopIteration:
        return None
