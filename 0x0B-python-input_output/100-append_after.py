#!/usr/bin/python3
"""Defines text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Function to insert text after each line containing goiven string.

    Args:
        filename: (str) Name of file.
        search_string: (str) string to search for within file.
        new_string: (str) string to insert.
    """
    txt = ""
    with open(filename) as r:
        for line in r:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)
