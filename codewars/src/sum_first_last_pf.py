"""Solution to Kata https://www.codewars.com/kata/https://www.codewars.com/kata/the-sum-of-the-first-and-the-last-prime-factor-make-chains-of-numbers/."""

def sflpf_data(val, nMax):
    """Return a sorted list of numbers whose first and last prime factor sum up to val."""
    out = []
    for n in range(4, end + 1):
        if n % 2:
            if is_prime(n):
                continue
        pf = prime_factors(n)
        if pf[0] + pf [-1] == val: out.append(n)
    return out


def is_prime(n):
    """Return True if n is prime."""
    if (n % 2 == 0 and n > 2) or n == 1:
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))


def prime_factors(n):
    """Return a list of prime factors for n."""
    factors = []
    p = 2
    while n >= (p * p):
        if n % p:
            p += 1
        else:
            n = n // p
            factors.append(p)
    factors.append(n)
    return factors
