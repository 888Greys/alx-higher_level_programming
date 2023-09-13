#!/usr/bin/python3
"""
This module provides a function to load JSON
data from a text file into a Python data structure (object).
"""
import json


def load_from_json_file(filename):
    """
    Load JSON data from the specified text
    file and return it as a Python data structure (object).

    :param filename: The name of the file
    containing the JSON data to be loaded.
    :return: A Python data structure (object)
    parsed from the JSON data in the file.
    """
    if filename == "":
        return
    with open(filename, "r") as f:
        return json.load(f)
