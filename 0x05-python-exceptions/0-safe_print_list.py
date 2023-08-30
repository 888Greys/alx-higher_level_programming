#!/usr/bin/python3
"""
    This Python code defines a function, `safe_print_list`,
    that safely prints the first `x` elements from a list,
    handling potential errors if there aren't enough elements to print.
    It returns the count of successfully printed elements.
"""


def safe_print_list(my_list=[], x=0):
    num = 0
    for j in range(x):
        try:
            print("{}".format(my_list[j]), end="")
            num += 1
        except IndexError:
            break
    print("")
    return (num)
