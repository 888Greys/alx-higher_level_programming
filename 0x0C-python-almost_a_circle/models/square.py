#!/usr/bin/python3
"""
Square class that inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Args:
        size (int): The size of the square.
        x (int): The x-coordinate of the square.
        y (int): The y-coordinate of the square.
        id (int): An optional identifier for the square.

    Attributes:
        size (int): The size of the square.

    Methods:
        update(): Update the attributes of the square.
        __str__(): Get a string representation of the square.
        to_dictionary(): Get a dictionary representation of
        the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square object.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            id (int): An optional identifier for the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Get the size of the square. """
        return self.width

    @size.setter
    def size(self, value):
        """ Set the size of the square. """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        argCount = len(args)
        if argCount == 0:
            if "id" in kwargs.keys():
                self.id = kwargs["id"]
            if "size" in kwargs.keys():
                self.size = kwargs["size"]
            if "x" in kwargs.keys():
                self.x = kwargs["x"]
            if "y" in kwargs.keys():
                self.y = kwargs["y"]
        if argCount > 0:
            self.id = args[0]
        if argCount > 1:
            self.size = args[1]
        if argCount > 2:
            self.x = args[2]
        if argCount > 3:
            self.y = args[3]

    def __str__(self):
        """ Get a string representation of the square. """
        string = "[{:s}] ({:d})".format(type(self).__name__, self.id)
        string += " {:d}/{:d} ".format(self.x, self.y)
        string += "- {:d}".format(self.size)
        return string

    def to_dictionary(self):
        """ Get a dictionary representation of the square. """
        dict_rec = {"x": self.x, "y": self.y, "id": self.id}
        dict_rec["size"] = self.size
        return dict_rec
