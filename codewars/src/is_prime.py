"""Module to solve the code-kata https://www.codewars.com/kata/is-a-number-prime/discuss/python."""

def is_prime(n):
    """Return True if n is a prime."""
    if abs(n) < 2:
        return False
    if n > 2 and n % 2 == 0:
        return False
    for x in range(3, int(n**0.5 + 1), 2):
        if n % x == 0:
            return False
    return True
