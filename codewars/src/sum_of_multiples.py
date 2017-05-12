"""This module solves kata https://www.codewars.com/kata/multiples-of-3-and-5/train/python."""


def solution(n):
    """Return a number representing the sum of multiples of 3 and 5 below given n."""
    cnt_first_multiple = [x for x in range(3, n, 3) if x % 10 not in [0, 5]]
    cnt_second_multiple = [x for x in range(5, n, 5)]
    return sum(cnt_first_multiple + cnt_second_multiple)

def better_solution(n):
    """Return a number representing the sum of multiples of 3 and 5 below given n in O(1) time."""
    def solution(number):
    a3 = (number-1)/3
    a5 = (number-1)/5
    a15 = (number-1)/15
    result = (a3*(a3+1)/2)*3 + (a5*(a5+1)/2)*5 - (a15*(a15+1)/2)*15
    return result
