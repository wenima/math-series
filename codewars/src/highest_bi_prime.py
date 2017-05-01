"""Module to solve https://www.codewars.com/kata/highest-number-with-two-prime-factors."""

def highest_biPrimefac(p1, p2, end):
    """Return a list with the highest number with prime factors p1 and p2, the
    exponent for the smaller prime and the exponent for the larger prime."""
    pass


def prime_factors(n):
    """Return a list with all prime factors of n."""
    factors = []
    p = 2
    while n >= (p * p):
        if n % p:
            p += 1
        else:
            n = n // p
            factors.append(p)
    factors.append(n)
    return factors
