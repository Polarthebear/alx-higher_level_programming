#!/usr/bin/python3
"""Defining a class MyInt which inherits from int."""


class MyInt(int):
    """== and != are inverted."""

    def __eq__(self, value):
        """== needs to behave like !=."""
        return self.real != value


    def __ne__(self, value):
        """!= needs to behave like ==."""
        return self.real == value
