#!/usr/bin/python3
"""defines function that returns JSON from string."""
import json


def from_json_string(my_str):
    """Return Python object representation of a JSON string."""
    return json.loads(my_str)
