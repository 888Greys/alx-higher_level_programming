#!/usr/bin/python3
"""
This Python code defines a function, `safe_print_list_integers`,
which safely prints the first `x` integers from a list.
It counts and returns the number of
successfully printed integers while gracefully
handling any non-integer elements in the list.
"""


def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for j in range(0, x):
        try:
            print("{:d}".format(my_list[j]), end="")
            num += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (num)
