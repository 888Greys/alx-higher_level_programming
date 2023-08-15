#!/usr/bin/python3
# This code prints the integers in a list

def print_list_integer(my_list=[]):
    for num in range(len(my_list)):
        print("{:d}".format(my_list[num]))
