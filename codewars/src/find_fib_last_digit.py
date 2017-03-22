"""This module solves kata https://www.codewars.com/kata/find-fibonacci-last-digit."""

def iter_fib(n):
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
    return b

def get_last_digit(n):
    return int(str(iter_fib(n))[-1])
