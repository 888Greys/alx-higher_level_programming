#!/usr/bin/python3
"""
A functio that prints a dictionary by ordered keys
"""


def print_sorted_dictionary(a_dictionary):
    all_sorted_keys = sorted(a_dictionary.keys())
    for a_key in all_sorted_keys:
        print("{} : {}".format(a_key, a_dictionary[a_key]))
