#!/usr/bin/python3
"""
Multiplying by using map
"""


def multiply_list_map(my_list=[], number=0):
    return (list(map((lambda i: i * number), my_list)))
# This function returns a list with all numbers multiplied
