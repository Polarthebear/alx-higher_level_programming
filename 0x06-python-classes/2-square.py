#!/usr/bin/python3

"""Defining a class square"""


class Square:
    """Representing a square."""

    def __init__(self, size=0):
        """Initializing the new square.


        Args:
        size = size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer.")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
