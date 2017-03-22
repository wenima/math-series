"""This module solves kata https://www.codewars.com/kata/find-fibonacci-last-digit."""

def get_last_digit(n):
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, (a+b) % 10
    return b
