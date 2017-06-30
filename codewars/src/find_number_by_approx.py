"""Solution for https://www.codewars.com/kata/these-arent-the-numbers-youre-looking-for-find-a-number-by-approximation/"""

def find_number(compare):
    """Takes in a compare function which takes the guessed number as parameter
    and returns 0 for the correct number, -1 if your number is smaller than the
    searched number and 1 if your guessed number is greater than the searched number.
    """
    start = 0
    end = 100
    guess = (start + end) // 2
    while True:
        if compare(guess) == 0:
            return guess
        elif compare(guess) == 1:
            end = guess
        elif compare(guess) == -1:
            start = guess
        guess = round((start + end) // 2, 5)
