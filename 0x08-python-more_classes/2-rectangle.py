#!/usr/bin/python3
"""

This is a Class Rectangle that defines a rectangle

"""


class Rectangle:
    """
    Creating a  Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        Initializes variables
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        returns width value of that
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets th width value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        returns height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets width value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        method to get area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        method to get perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2
