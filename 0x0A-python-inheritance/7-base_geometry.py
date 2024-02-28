#!/usr/bin/python3
"""Define a class BaseGeometry."""


class BaseGeometry:
    """Representing BaseGeometry."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """instance that validates parameter as int.


        Args:
            name (string): name of parameter
            value (int): value of parameter

        Raises:
            TypeError: if value not integer.
            valueError: less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
