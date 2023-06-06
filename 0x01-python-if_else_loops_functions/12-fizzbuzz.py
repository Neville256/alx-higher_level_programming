#!/usr/bin/python3
# 12-fizzbuzz.py

def fizzbuzz():
    """Print the number from 1 to 100 seperated by a space.

    For multiples of 3, print FIZZ instead of the number.
    For multiples of five, print BUZZ instead of the number.
    For mutliples of three and five, print FIZZBUZZ instead of the number."""
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FIZZBUZZ", end="")
        elif number % 3 == 0:
            print("FIZZ", end="")
        elif number % 5 == 0:
            print("BUZZ", end="")
        else:
            print("{}".format(number), end="")
