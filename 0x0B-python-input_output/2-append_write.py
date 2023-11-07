#!/usr/bin/python3
"""
A Python program that reads and prints lines from a text file.

Usage:
    - If 'nb_lines' is non-positive or zero, it reads
    and prints the entire file.
    - If 'nb_lines' is positive, it reads and prints the
    specified number of lines from the file.

Parameters:
    filename (str): The name of the file to read.
    nb_lines (int): The number of lines to read and print.
    If non-positive or zero, the entire file is printed.
"""


def read_lines(filename="", nb_lines=0):
    if filename == "":
        return
    if nb_lines <= 0:
        with open(filename, "r") as f:
            print(f.read(), end="")
    else:
        with open(filename, "r") as f:
            head = [next(f) for x in range(nb_lines)]
        print("".join(head), end="")
