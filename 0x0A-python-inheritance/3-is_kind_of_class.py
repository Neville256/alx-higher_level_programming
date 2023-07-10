#!/usr/bin/python3
"""
===================================
module with method is_kind_of_class
===================================
"""


def is_kind_of_class(obj, a_class):
    """Return True if an object is an instance of a class
    that inherited from the method"""

    return isinstance(obj, a_class)
