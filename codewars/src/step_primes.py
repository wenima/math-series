"""Module to solve the code-kata https://www.codewars.com/kata/steps-in-primes/python."""

def prime(a):
    """Return True if a is prime."""
    if a == 2: return True
    if a < 2 or a % 2 == 0: return False
    return not any(a % x == 0 for x in range(3, int(a**0.5) + 1, 2))


def step(g, m, n):
    """Return the first pair of primes between m and n with step g."""
    if m % 2 == 0: m += 1 #need to see an odd number so we can step over known composites
    try:
        return next([x, x + g] for x in range(m, n - g, 2) if prime(x) and prime(x + g))
    except StopIteration:
        return None
