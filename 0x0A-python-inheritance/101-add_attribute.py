#!/usr/bin/python3
"""Write a function that adds a new attribute to
an object if its possible:."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object

    Arguments:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add to
        object.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
