#!/usr/bin/python3
"""Define the class and inherited class function."""


def is_kind_of_class(obj, a_class):
    """"Checks if the object is an instance of, or if the object is 
    an instance of a class that inherited from, the specified class.

    Args:
        obj: object
        a_class: class to match

    Return:
        True (Success)
        False (Fail)
    """
    if isinstance(obj, a_class):
        return True
    return False
