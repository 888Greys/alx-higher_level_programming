#!/usr/bin/python3
"""
This function returns elements present in both sets
"""


def common_elements(set_1, set_2):
    common_set = set()
    for item in set_1:
        if item in set_2:
            common_set.add(item)
    return common_set
