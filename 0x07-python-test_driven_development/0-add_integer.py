#!/usr/bin/python3
def add_integer(a, b=98):
    """Check if they are ints or floats."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")

    """Casting to int."""
    a = int(a)
    b = int(b)

    """Return the sum of them"""
    return (a + b)
