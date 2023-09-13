#!/usr/bin/python3
"""
class Rectangle that inherits BaseGeometry
7-base geometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle of the code"""
    def __init__(self, width, height):
        """ initialize the validators """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
