#!/usr/bin/python3

"""Define a Python class MagicClass that does exactly the same as the provided bytecode."""

import math


class MagicClass:
    """Class representing a circle."""

    def __init__(self, radius=0):
        """Initializing the Magic Class.

        Args:
            radius (int/float): Radius of the MagicClass circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius


    def area(self):
        """Return the area of the class."""
        return (self.__radius ** 2 *math.pi)

    def circumference(self):
        """return the circumference of the circle."""
        return (2 * math.pi * self.__radius)
