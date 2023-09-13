#!/usr/bin/python3
"""
BaseGeometry - A base class for geometry-related operations.
"""


class BaseGeometry:
    """
    BaseGeometry is a base class for geometry-related operations.

    It provides methods for integer validation and serves
    as a foundation for defining
    more specialized geometry classes.

    Methods:
        integer_validator(self, name, value): Validate that
        a value is a positive integer.
        area(self): Calculate the area of a geometric shape
        (not implemented).
    """

    def integer_validator(self, name, value):
        """
        integer_validator(self, name, value) - Validate that a
        value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        """
        area(self) - Calculate the area of a geometric shape
        (not implemented).

        Raises:
            Exception: This method is not implemented and should
            be overridden in subclasses.
        """
        raise Exception("area() is not implemented")
