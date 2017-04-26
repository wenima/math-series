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


def get_next_prime(n, primes, direction=1):
    """Return the next prime of n in given direction."""
    if direction > 0:
        start = n + 1 if n % 2 == 0 else n + 2
        step = 2
        stop = n * n
    else:
        start = n -1 if n % 2 == 0 else n - 2
        step = -2
        stop = 0
    prime_generator = (x for x in xrange(start, stop, step) if prime(x, primes))
    return prime_generator.next()


def prime_bef_aft(n):
    """Return the first pair of primes between m and n with step g."""
    #n needs to start out as an odd number so we can step over known composites
    primes = [p for p in eratosthenes_step2(int(n // 2))]
    before = get_next_prime(n, primes, -1)
    after = get_next_prime(n, primes, 1)
    return [before, after]
