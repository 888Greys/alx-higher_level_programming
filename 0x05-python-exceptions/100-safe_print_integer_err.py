#!/usr/bin/python3
"""
This Python code imports the `sys` module and defines
a function called `safe_print_integer_err`.
The function attempts to print an integer value and returns
`True` if successful, or `False` if the value is not an
integer or cannot be printed as one. If an exception
(either `TypeError` or `ValueError`) occurs during
the printing process,
it prints the exception message to the standard
error (`sys.stderr`) and returns `False`.
"""


import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
