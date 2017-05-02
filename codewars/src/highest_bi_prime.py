"""Module to solve https://www.codewars.com/kata/highest-number-with-two-prime-factors."""

def highest_biPrimefac(p1, p2, end):
    """Return a list with the highest number with prime factors p1 and p2, the
    exponent for the smaller prime and the exponent for the larger prime."""
    given_primes = set([p1, p2])
    k1 = 0
    k2 = 0
    highest = 0
    for n in range(end, 0, -1):
        pf = prime_factors(n, given_primes)
        if given_primes == set(pf):
            if pf.count(p1) > k1 and pf.count(p2) > k2:
                k1 = pf.count(p1)
                k2 = pf.count(p2)
                highest = n
        if (p1 ** k1) * (p2 ** k2) > n:
            return [highest, k1, k2]
    return None

def prime_factors(n, given_primes):
    """Return a list with all prime factors of n."""
    factors = []
    if n < 2:
        return factors
    p = 2
    while n >= (p * p):
        if n % p:
            p += 1
        else:
            if p not in given_primes:
                return []
            n = n // p
            factors.append(p)
    factors.append(n)
    return factors
