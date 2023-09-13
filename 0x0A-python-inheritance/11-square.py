#!/usr/bin/python3
"""
Square - A class representing a square that inherits
from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """
    Square is a class representing a square that inherits
    from Rectangle.

    It provides methods for initializing the dimensions
    of the square,
    including its side length,
    and generating a string representation.

    Attributes:
        __size (int): The side length of the square.
    """
    def __init__(self, size):
        """
        Initialize a Square instance with the given side length.

        Args:
            size (int): The side length of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not greater than 0.
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        Generate a string representation of the square.

        Returns:
            str: A string representation in the format
            "[Square] size/size".
        """
        string = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return string
