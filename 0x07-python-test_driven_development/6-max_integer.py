#!/usr/bin/python3
"""Module to find max integer ina list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
    if the list is empty, function returns none
"""


if len(list) == 0:
    return None
result = list[0]
k = 1
while k < len(list):

    if list[k] > result:
        result = list[k]
    k += 1
return result
