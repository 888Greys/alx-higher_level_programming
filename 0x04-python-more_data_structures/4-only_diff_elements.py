#!/usr/bin/python3
# This code only returns elements present only in one set
def only_diff_elements(set_1, set_2):
    diff_set = set()

    for item in set_1:
        if item not in set_2:
            diff_set.add(item)

    for item in set_2:
        if item not in set_1:
            diff_set.add(item)

    return diff_set
