#!/usr/bin/python3
"""
This script defines a class named Rectangle, which represents a rectangle.
"""


class Rectangle:
    """
    Creates a Rectangle class for working with rectangles.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object with the specified width and height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle. Raises a TypeError for
        non-integer values and a ValueError for negative values.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle. Raises a TypeError for
        non-integer values and a ValueError for negative values.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        """
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        Returns a string representation of the rectangle,
        using '#' to represent its shape.
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            string += "\n"
            return string
        for i in range(self.__height):
            string += "#" * self.__width + "\n"
        return string[:-1]

    def __repr__(self):
        """
        Returns a string representation of the Rectangle object.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Deletes the Rectangle object and prints a farewell message.
        """
        print("Bye rectangle...")
