#!/usr/bin/python3
"""
This module provides a function to convert a
Python object to a dictionary representation
suitable for JSON serialization.
"""


def class_to_json(obj):
    """
    Convert the provided Python object to a
    dictionary representation.

    :param obj: The object to be converted
    to a dictionary.
    :return: A dictionary representing the
    provided object.
    """
    return vars(obj)
