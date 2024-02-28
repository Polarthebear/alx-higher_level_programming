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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
