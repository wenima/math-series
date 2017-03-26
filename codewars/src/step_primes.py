"""Module to solve the code-kata https://www.codewars.com/kata/steps-in-primes/python."""

from itertools import islice

def prime(a):
    """Return True if a is prime."""
    if a == 2: return True
    if a < 2 or a % 2 == 0: return False
    return not any(a % x == 0 for x in range(3, int(a**0.5) + 1, 2))


def find_next_prime(m, n):
    for i in range(m, n, 2):
        if prime(i):
            yield i


def step(g, m, n):
    """Return the first pair of primes between m and n with step g by recursively
    finding the next prime and check if that prime + steps is a prime and thus a match."""
    if m % 2 == 0: m += 1   #since we want to step over all even numbers, need to seed an odd number
    if prime(m) and prime(m + g):
        return [m, m + g]
    while m + g < n:
        m = next(find_next_prime(m + 2, n)) #gets the next prime from generator function
        return [m, m + g] if prime(m + g) else step(g, m, n) #call step recursively with next prime
