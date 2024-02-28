#!/usr/bin/python3
"""Defining a function which adds the attributes to objects."""


def add_attribute(obj, att, value):
    """Adds a attribute to objects if possible.

    Args:
        obj: object to add attribute to
        att: Name of attribute
        value: value of attribute

    Raises: 
        TypeError: if attribute cannoot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
