"""Module to solve kata https://www.codewars.com/kata/surrounding-primes-for-a-value/."""


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


def prime(n, primes):
    """Return True if a given n is a prime number, else False."""
    if n > 5 and n % 10 == 5:
        return False
    for p in primes:
        if n % p == 0:
            return False
    return True


def is_prime(a):
    """Return True if a is prime."""
    if a == 2: return True
    if a < 2 or a % 2 == 0: return False
    return not any(a % x == 0 for x in range(3, int(a**0.5) + 1, 2))


def prime_bef_aft(n):
    """Return the first pair of primes between m and n with step g."""
    #n needs to start out as an odd number so we can step over known composites
    primes = [p for p in eratosthenes_step2(int(n**0.5))]
    before = next(x for x in range(n - 1 if n % 2 == 0 else n -2, 0, -2) if prime(x, primes))
    after = next(x for x in range(n + 1 if n % 2 == 0 else n + 2, n * n, 2) if is_prime(x))
    return [before, after]
