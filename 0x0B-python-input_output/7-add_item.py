#!/usr/bin/python3
"""
Script for adding items to a JSON file.
"""

import json
from sys import argv
import os


def save_to_json_file(my_obj, filename):
    """
    Save the provided Python data structure (object)
    as JSON to the specified text file.

    :param my_obj: The Python data structure (object)
    to be saved as JSON.
    :param filename: The name of the file where the
    JSON data will be saved.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """
    Load JSON data from the specified text file and
    return it as a Python data structure (object).

    :param filename: The name of the file containing
    the JSON data to be loaded.
    :return: A Python data structure (object) parsed
    from the JSON data in the file.
    """
    with open(filename, "r") as f:
        return json.load(f)


if __name__ == '__main__':
    save_json_file = __import__("7-save_to_json_file").save_to_json_file
    load_json_file = __import__("8-load_from_json_file").load_from_json_file

    if not os.path.exists("add_item.json"):
        with open("add_item.json", "a") as f:
            pass
        save_json_file([], "add_item.json")

    save_json_file(load_json_file("add_item.json") + argv[1:], "add_item.json")
