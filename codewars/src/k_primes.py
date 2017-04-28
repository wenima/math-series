"""Module to solve https://www.codewars.com/kata/k-primes/python."""


def eratosthenes_step2(n):
    """Return all primes up to and including sqrt of n.
   Since we know primes can't be even, we iterate in steps of 2."""
    if n >= 2:
        yield 2
    multiples = set()
    for i in range(3, n+1, 2):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))


def prime_factors(n, primes, k):
    """Return a list of prime factors for a given number in ascending order if
    the number of prime factors equals k."""
    factors = []
    for p in primes:
        while True:
            if n % p:
                break
            else:
                n = n // p
                factors.append(p)
                if n < p:
                    return factors if len(factors) == k else None
                if len(factors) > k:
                    return None
    return factors if len(factors) == k else None


def get_primes(n):
    """Return a list of primes up to and including n."""
    return [p for p in eratosthenes_step2(n)]


def countKprimes(k, start, end):
    """Return a list of k-primes betwene start and end. A k-prime is a number
    which has exactly k primes, multiplicity counted. Before generating primes,
    we cap the range of primes to only those needed."""
    if end//2 ** (k -1) > 0:
        primes = get_primes(end//2 ** (k - 1))#only primes up to 2**(k-1) are possible prime factors
        return find_k_primes(k, start, end, primes)
    return []


def find_k_primes(k, start, end, primes=None):
    """Return a list of k-primes between start and end given a list of primes."""
    out = []
    for n in range(start, end + 1):
        if prime_factors(n, primes, k): out.append(n)
    return out
