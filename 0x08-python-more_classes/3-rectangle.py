#!/usr/bin/python3
"""
This script defines a class named Rectangle,
which is used to represent a rectangle.
"""


class Rectangle:
    """
    Creates a Rectangle class that provides
    functionality to work with rectangles.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object with the
        given width and height.
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
        Sets the width of the rectangle. Raises a TypeError
        for non-integer values and a ValueError for negative values.
        """
        if type(value) is not int:
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        If either width or height is 0, the perimeter is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        """
        Returns a string representation of the rectangle,
        using '#' to represent its shape.
        """
        string = ""
        if self.width == 0 or self.height == 0:
            string += "\n"
            return ""
        else:
            for i in range(self.height):
                string += "#" * self.width
                if i < self.height - 1:
                    string += "\n"
            return string
