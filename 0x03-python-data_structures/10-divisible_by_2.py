#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """Find all multiple of 2 in a list."""
    multiple = []
    for k in range(len(my_list)):
        if my_list[k] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)
    return(multiples)
