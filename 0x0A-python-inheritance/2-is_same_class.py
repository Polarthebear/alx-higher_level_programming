#!/usr/bin/python3
"""Function that checks a class."""


def is_same_class(obj, a_class):
    """Check if object is exactly an instance of the specified class.

    Args:
        obj: object
        a_class: class to match
    Returns:
        True (success).
        False (Fail).
    """
    if type(obj) is a_class:
        return True
    return False
