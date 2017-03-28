"""Module to solve the code-kata https://www.codewars.com/kata/pure-odd-digits-primes."""

def isPrime(n):
    """Return True if n is a prime."""
    if n > 2 and n % 2 == 0:
        return False
    for x in range(3, int(n**0.5 + 1), 2):
        if n % x == 0:
            return False
    return True


def erastothenes(n):
    """Return all primes up to and including n if n is a prime."""
    multiples = set()
    for i in range(2, n + 1):
        if i not in multiples:
            yield
            multiples.update(range(i * i, n + 1, i))


def step(g, m, n):
    """Return the first pair of primes between m and n with step g."""
    if m % 2 == 0: m += 1 #need to see an odd number so we can step over known composites
    try:
        return next([x, x + g] for x in range(m, n - g, 2) if prime(x) and prime(x + g))
    except StopIteration:
        return None


def only_oddDigPrimes(n):
    """Return a list containing three numbers: number of pure digit primes, largest pure digit prime
    smaller than n and next pure digit prime after n. If n is itself a pure digit prime, include in count."""
    pass
