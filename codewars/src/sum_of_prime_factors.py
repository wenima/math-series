"""Solution to Kata https://www.codewars.com/kata/the-sum-of-the-prime-factors-of-a-number-dot-dot-dot-what-for."""

def is_prime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return n > 1


def prime_factors(n):
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


def mult_primefactor_sum(start, stop):
    out = []
    for n in range(start, stop + 1):
        if is_prime(n):
            continue
        if n % sum(prime_factors(n)) == 0:
            out.append(n)
    return out
