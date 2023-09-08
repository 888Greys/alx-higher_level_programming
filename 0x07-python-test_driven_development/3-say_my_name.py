#!/usr/bin/python3
# 3-say_my_name.py
"""Defines a function that prints a name."""


def say_my_name(first_name, last_name=""):
    """Print a name

    Arguements:
        first_name (string): The first name to print.
        last_name (string): The last name to print.
    Raises:
        TypeError: If either of first_name or last_name are not string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
