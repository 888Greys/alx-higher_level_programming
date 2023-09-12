#!/usr/bin/python3
"""
Defines a Rectangle class that represents a rectangle.

A rectangle is a geometric shape with four sides, where
opposite sides are
equal in length, and all angles are 90 degrees.
"""


class Rectangle:
    """
    Represents a rectangle with width and height.

    Attributes:
        number_of_instances (int): A class attribute that keeps track of the
        number of Rectangle instances created.
        print_symbol (str): A class attribute that determines the symbol used
        when representing the rectangle as a string.

    Methods:
        __init__(self, width=0, height=0): Initializes a new
        Rectangle instance.
        area(self): Calculates the area of the rectangle.
        perimeter(self): Calculates the perimeter of the rectangle.
        __str__(self): Converts the rectangle to a string representation.
        __repr__(self): Returns a string representation of the
        Rectangle object.
        __del__(self): Destructor method to clean up and print a message.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        Convert the rectangle to a string representation using
        print_symbol.

        Returns:
            str: A string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """
        Return a string representation of the Rectangle object.

        Returns:
            str: A string representation of the rectangle in the format
            "Rectangle(width, height)".
        """
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """
        Destructor method to decrease the number_of_instances
        attribute and print
        a message.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
