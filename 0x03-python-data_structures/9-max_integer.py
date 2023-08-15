#!/usr/bin/python3
"""
a function that prints the biggest
integer of alist
"""


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    huge = my_list[0]
    for num in range(len(my_list)):
        if my_list[num] > huge:
            huge = my_list[num]

    return (huge)
