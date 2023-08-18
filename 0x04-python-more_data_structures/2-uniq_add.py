#!/usr/bin/python3
def uniq_add(my_list=[]):
    """This function adds all integers in a list"""
    different_list = set(my_list)

    number = 0

    for j in different_list:
        number += j
    return (number)
