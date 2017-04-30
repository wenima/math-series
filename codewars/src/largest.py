"""Module to solve the code-kata https://www.codewars.com/kata/largest-prime-number-containing-n-digit/."""

def is_prime(n):
    """Return True if n is a prime."""
    if (n % 2 == 0 and n > 2) or n == 1:
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))


def largest(n):
    """Return the largest prime with n digits."""
    try:
        if n < 1 : return False
    except TypeError:
        return False
    start = int(''.join(['9' for i in range(n)]))
    for n in range(start, start - (10 ** n - 1) + 1, -2):
        if is_prime(n):
            return n
    return False
