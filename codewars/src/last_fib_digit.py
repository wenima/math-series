"""This module solves kata http://www.codewars.com/kata/find-last-fibonacci-digit-hardcore-version/python."""

from math import sqrt

def last_fib_digit(n):
    pisano_mod_10 = generate_pisano_sequence_10(n)
    return pisano_mod_10[n % 60 - 1]


def generate_pisano_sequence_10(n):
    return [int(((sqrt(5) + 1) / 2) ** n / sqrt(5) + 0.5) % 10 for n in range(1, 61)]
