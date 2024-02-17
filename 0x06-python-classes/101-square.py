#!/usr/bin/python3

"""Defining a class Square"""


class Square:
    """Representing a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing a new square

        Args:
            size = size of the new square
            position = position of new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getting the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returning current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Printing the square with the # characters."""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    def __str__(self):
        """defining the print() representation of the square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for n in range(0, slef.__size):
            [print(" ", end="") for i in range(0, slef.__position[0])]
            [print('#', end="") for n in range(0, self.__size)]
            if n != self.__size - 1:
                print("")
        return ("")