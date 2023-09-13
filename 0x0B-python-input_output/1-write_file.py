#!/usr/bin/python3
"""
This program writes text to a file.
"""


def write_file(filename="", text=""):
    """
    Write the specified text to the given file
    and return the number of characters written.

    :param filename: The name of the file to write to.
    :param text: The text to be written to the file.
    :return: The number of characters written
    to the file.
    """
    if filename == "":
        return 0
    with open(filename, "w") as f:
        f.write(text)
    return len(text)
