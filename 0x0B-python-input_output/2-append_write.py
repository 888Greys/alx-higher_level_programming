#!/usr/bin/python3
"""
This program appends text to a file.
"""


def append_write(filename="", text=""):
    """
    Append the specified text to the given file
    and return the number of characters written.

    :param filename: The name of the file to which
    text will be appended.
    :param text: The text to be appended to the file.
    :return: The number of characters appended to
    the file.
    """
    if filename == "":
        return 0
    with open(filename, "a") as f:
        f.write(text)
    return len(text)
