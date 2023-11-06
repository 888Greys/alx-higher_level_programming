#!/usr/bin/python3
""" Define a function add_attribute that attempts
to add a new attribute to an object
"""


def add_attribute(a, name, other):
    """ Attempt to add a new attribute to an object,
    and raise a TypeError if the operation is not allowed.

    Args:
        a (object): The target object to which the
        attribute should be added.
        name (str): The name of the new attribute.
        other (any): The value or content of the new attribute.
    Raises:
        TypeError: If adding a new attribute is not allowed.
    """
    raise TypeError("can't add a new attribute")
