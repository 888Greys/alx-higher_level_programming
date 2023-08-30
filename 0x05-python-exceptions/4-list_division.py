#!/usr/bin/python3
"""
This Python code defines a function, `list_division`,
that takes two lists,
`my_list_1` and `my_list_2`, along with a specified `list_length`.
It iterates through both lists up to the given length,
performing division element-wise. The code handles several
types of exceptions, including type mismatches, division by zero,
and index out of range errors, and appends the result
(or `0` in case of an error) to a new list.
The function returns this new list containing
thedivision results or error placeholders.
"""


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
