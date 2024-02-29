#!/usr/bin/python3
"""defines function that returns JSON from string."""
import json


def load_from_json_file(filename):
    """Make python object using JSON file."""
    with open(filename) as f:
        return json.load(f)
