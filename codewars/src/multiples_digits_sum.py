"""This module solves kata https://www.codewars.com/kata/multiples-and-digit-sums/train/python."""


def procedure(i):
    """Return an integer derived by first finding all multiples of i up to 100,
    then summing all up digit sums of all multiples."""
    return sum(int(d) for i in range(n, 101, n) for d in str(i))
