#!/usr/bin/python3
"""
inherits_from - Check if an object is an instance of
a class that inherits from the specified class.

This function returns True if the object is an instance
of a class that inherited from the specified class.

Args:
    obj: The object to check.
    a_class: The class to compare the object against.

Returns:
    True if the object is an instance of a class that
    inherits from the specified class, False otherwise.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that
    inherits from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare the object against.

    Returns:
        True if the object is an instance of a class that
        inherits from the specified class, False otherwise.
    """
    return issubclass(type(obj), a_class) and not type(obj) is a_class
