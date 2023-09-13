#!/usr/bin/python3
"""
This module provides a function to convert a
JSON string into a Python data structure (object).
"""
import json


def from_json_string(json_str):
    """
    Return a Python data structure (object)
    represented by the provided JSON string.

    :param json_str: A JSON-formatted string
    to be converted into a Python object.
    :return: A Python data structure (object)
    parsed from the input JSON string.
    """
    return json.loads(json_str)
