"""Module to solve the code-kata https://www.codewars.com/kata/goldbachs-conjecture-prime-numbers."""

from itertools import islice


def eratosthenes_step2(n):
    """Return all primes up to and including n if n is a prime
   Since we know primes can't be even, we iterate in steps of 2."""
    if n >= 2:
        yield 2
    multiples = set()
    for i in range(3, n+1, 2):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))


def goldbach(even_number):
    """Return a list of prime pairs which sum up to even_number."""
    out = []
    primes = [p for p in eratosthenes_step2(even_number - 2)]
    for idx, p in enumerate(primes):
        if p * 2 > even_number:
            break
        for pp in islice(primes, idx, None):
            if p + pp > even_number:
                break
            if p + pp == even_number:
                out.append([p, pp])
    return out
