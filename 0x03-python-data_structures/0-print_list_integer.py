#!/usr/bin/python3
"""
This code prints all the integers of a list
"""

def print_list_integer(my_list=[]):
    for num in range(len(my_list)):
        print("{:d}".format(my_list[num]))
