#!/usr/bin/python3
"""
This module provides a function to convert
an object to its JSON representation (string).
"""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of the
    provided object as a string.

    :param my_obj: The object to be converted to JSON.
    :return: A JSON-formatted string
    representation of the input object.
    """
    return json.dumps(my_obj)
