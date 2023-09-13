#!/usr/bin/python3
"""
This module provides a function to save a
Python data structure (object) as JSON to a text file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Save the provided Python data structure
    (object) as JSON to the specified text file.

    :param my_obj: The Python data structure
    (object) to be saved as JSON.
    :param filename: The name of the file where
    the JSON data will be saved.
    """
    if filename == "":
        return
    with open(filename, "w") as f:
        json.dump(my_obj, f)
