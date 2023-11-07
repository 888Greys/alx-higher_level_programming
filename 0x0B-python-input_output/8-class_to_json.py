#!/usr/bin/python3
"""Defines a Python class-to-JSON dictionary
conversion function."""


def class_to_json(obj):
    """
    Convert a Python class instance to a
    JSON-compatible dictionary.

    Args:
        obj: A Python class instance.

    Returns:
        dict: A dictionary representation of
        the class's attributes.
    """
    return obj.__dict__
