#!/usr/bin/python3
"""Defining a python class-to-JSON function."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure."""
    return obj.__dict__
