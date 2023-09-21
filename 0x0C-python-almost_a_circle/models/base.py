#!/usr/bin/python3

import json
import turtle


class Base:
    """
    Base class for managing objects.

    This class provides essential methods for object serialization,
    deserialization, and drawing using the 'turtle' module.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
            id (int): An optional identifier for the object.
            If not provided, it will be automatically assigned.
        """
        if id is None:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries to be converted.

        Returns:
            str: A JSON string representation of the input list of
            dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects as a JSON string representation to a file.

        Args:
            list_objs (list): A list of objects to be serialized and
            saved to a file.
        """
        LO_dict = []
        if list_objs is not None:
            LO_dict = [x.to_dictionary() for x in list_objs]
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(LO_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string representation to a list of dictionaries.

        Args:
            json_string (str): A JSON string to be converted.

        Returns:
            list: A list of dictionaries parsed from the JSON string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance of the class and return it, initializing it
        with values from a dictionary.

        Args:
            dictionary (dict): A dictionary containing attributes to
            initialize the object.

        Returns:
            Base: An instance of the class with attributes set from
            the input dictionary.
        """
        if cls.__name__ == "Rectangle":
            inst = cls(1, 1)
        elif cls.__name__ == "Square":
            inst = cls(1)
        else:
            return None
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances from a JSON file.

        Returns:
            list: A list of instances created from the data
            stored in a JSON file.
        """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                contentRead = f.read()
        except FileNotFoundError:
            return []
        listOfDicts = cls.from_json_string(contentRead)
        return [cls.create(**inst) for inst in listOfDicts]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw a list of rectangles and squares using the 'turtle' module.

        Args:
            list_rectangles (list): A list of Rectangle objects to be drawn.
            list_squares (list): A list of Square objects to be drawn.
        """
        for rec in list_rectangles:
            rec = rec.to_dictionary()
            turtle.up()
            turtle.setx(rec["x"])
            turtle.sety(rec["y"])
            turtle.down()
            turtle.fd(rec["width"])
            turtle.right(90)
            turtle.fd(rec["height"])
            turtle.right(90)
            turtle.fd(rec["width"])
            turtle.right(90)
            turtle.fd(rec["height"])

        for square in list_squares:
            size = square["size"]
            turtle.up()
            turtle.setx(square["x"])
            turtle.sety(square["y"])
            turtle.down()
            turtle.fd(size)
            turtle.right(90)
            turtle.fd(size)
            turtle.right(90)
            turtle.fd(size)
            turtle.right(90)
            turtle.fd(size)
            turtle.right(90)
