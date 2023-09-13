#!/usr/bin/python3
"""
Rectangle - A class representing a rectangle that inherits
from BaseGeometry.
"""

# Import the BaseGeometry class from the '7-base_geometry' module
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle is a class representing a rectangle that inherits from
    BaseGeometry.

    It provides methods for initializing the dimensions of the rectangle
    and for integer validation.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not greater than 0.
        """
        # Validate and set the width and height attributes
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
