"""Module to solve https://www.codewars.com/kata/k-primes/python."""

def count_factors(n):
    t, d, q, m = 2, 5, 2 + n % 2, int(n ** .5)
    while q <= m and n % q:
        t, d, q = 6-t, d+t, d
    return q <= m and 1 + count_factors(n // q) or n > 1

def count_Kprimes(k, start, end):
    return [n for n in xrange(start, end + 1) if count_factors(n) == k]

def puzzle(s):
    p1, p3, p7 = [set(count_Kprimes(p, 0, s)) for p in (1, 3, 7)]
    return sum(s-b-c in p1 for c in p7 for b in p3)
