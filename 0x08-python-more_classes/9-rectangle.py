#!/usr/bin/python3
"""
This script defines a class named Rectangle,
which represents a rectangle.
"""


class Rectangle:
    """
    Create Rectangle class to define and manipulate rectangles.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object with the specified
        width and height. Also increments the instance count.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        Sets the height of the rectangle. Raises a TypeError
        for non-integer values and a ValueError for negative values.
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
        using the specified print symbol to represent its shape.
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            string += "\n"
            return string
        for i in range(self.__height):
            string += str(self.print_symbol) * self.__width + "\n"
        return string[:-1]

    def __repr__(self):
        """
        Returns a string representation of the Rectangle object.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Deletes the Rectangle object, prints a farewell message,
        and decrements the instance count.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and returns the one with a greater area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle with equal sides (square).
        """
        return cls(size, size)
