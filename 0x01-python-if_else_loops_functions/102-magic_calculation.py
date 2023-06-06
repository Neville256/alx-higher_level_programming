#!/usr/bin/python3
# 102-magic_calculation.py

def magic_calculations(a, b, c):
    """Match bytecode provided by Holberton School."""
    if a < b:
        return(c)
    if c > b:
        return(a + b)
    return(a*b - c)
