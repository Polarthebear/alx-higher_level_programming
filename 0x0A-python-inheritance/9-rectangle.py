#!/usr/bin/python3
"""Definition of class (Rectangle) that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializing new Rectangle.

        Args:
            width(int): width of the rectanhle.
            height(int): height of the rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Returning the print() and str() reps of a rectangle."""
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__width, self.__height)
