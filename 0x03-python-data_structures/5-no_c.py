#!/usr/bin/python3
"""
A function that removes all the characters c and
C from a string
"""


def no_c(my_string):
    copy = [num for num in my_string if num != 'c' and num != 'C']
    return ("".join(copy))
