"""This module defines functions that implement mathematical series."""

from math import sqrt


def fibonacci(n):
    """Return the nth number in the fibonacci series."""
    return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))


def lucas(n):
    """Return the nth number in the lucas series."""
    return sum_series(n, 2, 1)


def sum_series(n, first=0, second=1):
    """Determine nth number in series with starting values of first and second."""
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n - 1, first, second) + sum_series(n - 2, first, second)


if __name__ == "__main__":
    output = """
    This code houses the fibonacci and lucas functions.
    ...

    fibonacci(n):
    Return the nth number in the fibonacci series.

    lucas(n):
    Return the nth number in the lucas series.

    sum_series(n, first=0, second=1):
    Determine nth number in series with starting values of first and second.
    """
    print(output)
    print("\texamples")
    print("\t>>>fibonacci(2): ", fibonacci(2))
    print("\t>>>lucas(3): ", lucas(3))
    print("\t>>>sum_series(4, 3, 3): ", sum_series(4, 3, 3))
    fibonacci(30)
    fibonacci(40)
    fibonacci(50)
    fibonacci(80)
