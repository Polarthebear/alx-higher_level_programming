#!/usr/bin/python3

"""Defining a class Square"""


class Square:
    """Representing a square."""

    def __init__(self, size=0):
        """Initializing a new square.

        Args:
            size: Size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
