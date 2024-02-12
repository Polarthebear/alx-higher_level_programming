#!/usr/bin/python3
"""Defines a rectangle by: (based on 1-rectangle.py)"""

class Rectangle:
    """Representing a rectangle"""


    def __init__(self, width=0, height=0):
        """ Initializing a new rectangle.

        Args:
        width (int): width of the rectangle
        height (int): height of the rectangle.
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            """setting width attribute"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            """setting height attribute"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

        def area(self):
            """return the area of the particular rectangle."""
            return (self.__width * self.__height)

        def perimeter(self):
            """Return the perimeter of the particular rectangle."""
            if self.__width == 0 or self.__height == 0:
                return (0)
            else:
                return ((self.width * 2) + (self.__height * 2))
