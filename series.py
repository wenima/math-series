"""This code houses the fibonacci and lucas functions."""


def fibonacci(n):
    """Return the nth number in the fibonacci series."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """Return the nth number in the lucas series."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


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
