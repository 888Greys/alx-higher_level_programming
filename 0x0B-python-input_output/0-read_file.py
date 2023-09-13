#!/usr/bin/python3
"""
This program prints the contents of a
text file to stdout.
"""


def read_file(filename=""):
    """
    Prints the contents of the specified file to stdout.

    :param filename: The name of the file to read.
    """
    if filename == "":
        return
    with open(filename, "r") as f:
        print(f.read(), end="")
