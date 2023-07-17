#!/usr/bin/python3
"""
Module for append_after method.
"""


def append_after(filename="", search_string="", new_string=""):
    '''Method for inserting text after search string.'''
    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        k = 0
        while i < len(lines):
            if search_string in lines[k]:
                lines[k:k + 1] = [lines[k], new_string]
                k += 1
            k += 1
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)
