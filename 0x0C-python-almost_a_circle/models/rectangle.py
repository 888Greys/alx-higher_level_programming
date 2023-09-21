#!/usr/bin/python3
"""
Rectangle class that inherits from Base.
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle.
        y (int): The y-coordinate of the rectangle.
        id (int): An optional identifier for the rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The x-coordinate of the rectangle.
        __y (int): The y-coordinate of the rectangle.

    Methods:
        area(): Calculate the area of the rectangle.
        display(): Display the rectangle using '#' characters.
        __str__(): Get a string representation of the rectangle.
        update(): Update the attributes of the rectangle.
        to_dictionary(): Get a dictionary representation of the
        rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.
            id (int): An optional identifier for the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Get the width of the rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width of the rectangle. """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Get the height of the rectangle. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height of the rectangle. """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Get the x-coordinate of the rectangle. """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set the x-coordinate of the rectangle. """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Get the y-coordinate of the rectangle. """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set the y-coordinate of the rectangle. """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculate the area of the rectangle. """
        return self.__height * self.__width

    def display(self):
        """ Display the rectangle using '#' characters. """
        for v_shift in range(self.__y):
            print()
        for height in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ Get a string representation of the rectangle. """
        string = "[{:s}] ({:d})".format(type(self).__name__, self.id)
        string += " {:d}/{:d} ".format(self.__x, self.__y)
        string += "- {:d}/{:d}".format(self.__width, self.__height)
        return string

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        argCount = len(args)
        if argCount == 0:
            if "id" in kwargs.keys():
                super().__init__(kwargs["id"])
            if "width" in kwargs.keys():
                self.width = kwargs["width"]
            if "height" in kwargs.keys():
                self.height = kwargs["height"]
            if "x" in kwargs.keys():
                self.x = kwargs["x"]
            if "y" in kwargs.keys():
                self.y = kwargs["y"]
        if argCount > 0:
            super().__init__(args[0])
        if argCount > 1:
            self.width = args[1]
        if argCount > 2:
            self.height = args[2]
        if argCount > 3:
            self.x = args[3]
        if argCount > 4:
            self.y = args[4]

    def to_dictionary(self):
        """ Get a dictionary representation of the rectangle. """
        dict_rec = {"x": self.__x, "y": self.__y, "id": self.id}
        dict_rec["width"] = self.__width
        dict_rec["height"] = self.__height
        return dict_rec
