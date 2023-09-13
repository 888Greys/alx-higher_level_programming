#!/usr/bin/python3
"""
Rectangle - A class representing a rectangle that
inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle is a class representing a rectangle that
    inherits from BaseGeometry.

    It provides methods for initializing the dimensions of
    the rectangle, calculating its area,
    and generating a string representation.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with the given width
        and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not greater than 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Generate a string representation of the rectangle.

        Returns:
            str: A string representation in the format
            "[Rectangle] width/height".
        """
        string = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return string
