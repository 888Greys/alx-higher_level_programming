#!/usr/bin/python3
"""
Program that counts  the  lines of code in a file
"""


def number_of_lines(filename="an.py"):
    """ it counts the lines in file """
    count = 0
    if filename == "":
        return count
    with open(filename, "r") as f:
        for i in f:
            count += 1
    return count
