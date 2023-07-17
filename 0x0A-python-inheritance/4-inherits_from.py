#!/usr/bin/python3
"""
===================================
module with method inherits_from
===================================
"""


def inherits_from(obj, a_class):
    """Return True if an object is an instance of a class
    that inherited from the Method"""

    return False if type(obj) is a_class else isinstance(obj, a_class)
