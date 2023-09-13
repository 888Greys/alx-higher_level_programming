#!/usr/bin/python3
"""
is_kind_of_class - Check if an object is an instance of,
or inherits from, the specified class.

This function returns True if the object is an instance of
the specified class or if the object is an instance of a
class that inherits from the specified class.

Args:
    obj: The object to check.
    a_class: The class to compare the object against.

Returns:
    True if the object is an instance of the specified class
    or inherits from it, False otherwise.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or inherits from,
    the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare the object against.

    Returns:
        True if the object is an instance of the specified
        class or inherits from it, False otherwise.
    """
    return isinstance(obj, a_class)
