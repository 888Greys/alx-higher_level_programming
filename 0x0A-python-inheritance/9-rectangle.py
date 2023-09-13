#!/usr/bin/python3
""" square#1  class """
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """ square: its really working """
    def __init__(self, size):
        """ initialization """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
