#!/usr/bin/python3
"""
This Python code defines a function, `raise_exception_msg`,
which raises a `NameError` exception with an optional
custom error message provided as an argument.
It demonstrates how to raise a specific exception
with a user-defined error message.
"""


def raise_exception_msg(message=""):
    raise NameError(message)
