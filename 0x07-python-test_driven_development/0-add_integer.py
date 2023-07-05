#!/usr/bin/python3
# 0-add_integer.py
"""Defines an integer addition function."""


def add_integer(a=None, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition.

    Raises:
        TypeError: If either a or b is non-integer and non-float.
        ValueError: If a or b cannot be converted to integers.
    """
    if a is None:
        raise TypeError(
            "add_integer() missing 1 required positional argument: 'a'"
        )
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    try:
        return int(a) + int(b)
    except ValueError:
        raise ValueError("a or b cannot be converted to integers")
