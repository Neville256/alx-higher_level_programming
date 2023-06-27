#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a Square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): size of new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set current size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Print square # character."""
        for _ in range(0, self.__size):
            [print("#", end="") for _ in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
