#!/usr/bin/python3
""" Definition of the Square class that inherits from Rectangle """

Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """ Define the Square class, a specific type of rectangle """

    def __init__(self, size):
        """ Initialize a new Square instance with a given side length.

        Args:
            size (int): The side length of the square.
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """ Return a string representation of the Square object.

        Returns:
            str: A string representation in the format "[Square] size/size".
        """
        string = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return string
