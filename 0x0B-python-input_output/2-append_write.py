#!/usr/bin/python3
"""Defines a function that reads a text file."""


def append_write(filename="", text=""):
    """Function that writes appends to UTF8 text file.


    Args:
        filename: name of file to write to
        text: text to write to file.
    Return:
        Number of characters that have been written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
