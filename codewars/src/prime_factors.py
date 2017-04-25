"""Module to solve https://www.codewars.com/kata/prime-factors."""


def prime_factors(n):
    """Return a list of prime factors for a given number in ascending order."""
    factors = []
    p = 2
    if n < 2:
        return factors
    while n >= (p * p):
        if n % p:
            p += 1
        else:
            n = n // p
            factors.append(p)
    factors.append(n)
    return factors
