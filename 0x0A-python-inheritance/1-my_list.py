#!/usr/bin/python3
"""Class that inherits from list."""

class MyList(list):
    """representing MyList class."""

    def print_sorted(self):
        """Print list in ascending order."""
        print(sorted(self))
