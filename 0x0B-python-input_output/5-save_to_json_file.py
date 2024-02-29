#!/usr/bin/python3
"""defines function that returns JSON from string."""
import json


def save_to_json_file(my_obj, filename):
    """Writes object to text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
