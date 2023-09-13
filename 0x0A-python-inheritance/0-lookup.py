#!/usr/bin/python3

"""
This module provides a function for looking up the attributes
and methods of an object.
"""


def lookup(obj):
    """
    This function takes an object as input and returns a list
    of available attributes and methods of that object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the attributes
        and methods of the object.
    """
    return dir(obj)
