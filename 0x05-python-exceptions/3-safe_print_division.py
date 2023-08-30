#!/usr/bin/python3

"""
This Python code defines a function, `safe_print_division`,
which attempts to perform division between two numbers, `a` and `b`.
It handles potential errors, including division by zero and type mismatches,
and prints the result (or `None` if an error occurs)
before returning the result.
"""


def safe_print_division(a, b):
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
