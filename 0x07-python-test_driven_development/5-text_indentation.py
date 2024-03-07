#!/usr/bin/python3
"""Defines function that indents text."""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :.


    Args:
        text: (string) Text to print

    Raises:
        TypeError: If text is not string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    ch = 0
    while ch < len(text) and text[ch] == ' ':
        ch += 1

    while ch < len(text):
        print(text[ch], end="")
        if text[ch] == "\n" or text[ch] in ".?:":
            if text[ch] in ".?:":
                print("\n")
            ch += 1
            while ch < len(text) and text[ch] == ' ':
                ch += 1
            continue
        ch += 1
