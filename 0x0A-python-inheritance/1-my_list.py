#!/usr/bin/python3
"""
===========================
Module with class MyList
===========================
"""


class MyList(list):
    """method print_sorted with class"""

    def print_sorted(self):
        """sorted list of a method"""

        print(sorted(list(self)))
