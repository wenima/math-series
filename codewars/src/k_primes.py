"""Module to solve https://www.codewars.com/kata/k-primes/python."""

from collections import defaultdict
from itertools import takewhile

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
    if k == 1 and n in primes:
        factors.append(n)
        return factors
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


def count_Kprimes(k, start, end):
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
    if k == 1:
        for p in takewhile(lambda x: x <= end, primes):
                out.append(p)
                return out
    if start < 2 ** (k + 1): start = 2 ** k
    for n in xrange(start, end + 1):
        if k != 1 and n in primes:
            continue
        if out and n - 1 == out[-1] and k > 3:
            continue
        if prime_factors(n, primes, k, out): out.append(n)
    return out


def find_largest_k_prime(k, n):
    """Return the largest k prime for given n."""
    if 2 ** k < n < 2 ** (k + 1):
        prime = 2 ** k
        return ((2 ** k), n - prime)
    else:
        return 0, 0

def puzzle_pieces(n):
    """Return a dictionary holding all 1, 3, and 7 k primes."""
    kprimes = defaultdict(list)
    kprimes = {key : [] for key in [7, 3, 1]}
    upper = 0
    for k in kprimes.keys():
        print(k)
        if k == 7:
            prime, upper = find_largest_k_prime(k, n)
            if not prime:
                return []
            kprimes[k].append(prime)
        if k == 3:
            kprimes[k].extend(count_Kprimes(k, 2, upper))
            upper -= kprimes[k][0]
        if k == 1:
            primes = get_primes(upper)
            for p in takewhile(lambda x: x <= upper, primes):
                kprimes[k].append(p)
    return kprimes


def puzzle(n):
    """Return the number of combinations 1, 3, 7 k primes can make to sum up to target."""
    pieces = puzzle_pieces(n)
    if not pieces:
        return 0
    target = n - pieces[7][0]
    return len([(num, v) for num in pieces[3] for v in pieces[1] if num + v == target])
