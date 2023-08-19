#!/usr/bin/python3
"""
A function that returns all values
multiplied by two
"""


def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()
    list_keys = list(new_dir.keys())

    for i in list_keys:
        new_dir[i] *= 2

    return (new_dir)
# actually working
