#!/usr/bin/python3
"""defines function that returns JSON from string."""
import json


def to_json_string(my_obj):
    """return JSON representation of an obj(string)."""
    return json.dumps(my_obj)
