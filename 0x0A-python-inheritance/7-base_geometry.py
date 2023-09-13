#!/usr/bin/python3
"""
class BaseGeometry
almost cried trying this
"""


class BaseGeometry:
    """ class BaseGeometry: I have done it"""
    def integer_validator(self, name, value):
        """ int validator """
        if not type(value) is int:
            raise TypeError(str(name) + " must be an integer")
        if value <= 0:
            raise ValueError(str(name) + " must be greater than 0")

    def area(self):
        """ public instance method not implemented"""
        raise Exception("area() is not implemented")
