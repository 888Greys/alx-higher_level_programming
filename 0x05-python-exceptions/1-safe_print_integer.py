#!/usr/bin/python3
"""
This Python code defines a function, `safe_print_integer`,
that attempts to print an integer value and returns
`True` if successful, or `False`
if the value is not an integer or cannot be printed as one.
"""


def safe_print_integer(value):

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
