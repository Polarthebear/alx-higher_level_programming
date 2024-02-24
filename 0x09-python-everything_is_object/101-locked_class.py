#!/usr/bin/python3
"""Define a locked class."""


class LockedClass:
    """Stop user from instatiating  new LockedClass attri,
    for everything but 'first_name'.
    """

    __slots__ = ["first_name"]
