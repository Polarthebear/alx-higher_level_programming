#!/usr/bin/python3

"""Defining a class Square"""


class Square:
    """Representing a square"""

    def __init__(self, size=0):
        """Initializing a new square

        Args:
            size = size of the new square
        """
        self.size = size

    @property
    def size(self):
        """Get current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        """Returning current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Printing the square with the # character."""
        for n in range(0, self.__size):
            [print("#", end="") for m in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
