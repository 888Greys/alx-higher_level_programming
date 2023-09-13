#!/usr/bin/python3
"""
This module defines a Student class.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student object.

        :param first_name: The first name of the student.
        :param last_name: The last name of the student.
        :param age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary representation of the Student object.

        :param attrs: A list of attribute names to include
        in the dictionary (default is None).
        :return: A dictionary representing the Student object.
        """
        if attrs is None:
            return vars(self)
        return {attr: getattr(self, attr, None) for attr in attrs}

    def reload_from_json(self, json):
        """
        Update the Student object with data from a JSON
        dictionary.

        :param json: A dictionary containing student data
        in JSON format.
        """
        for key, value in json.items():
            setattr(self, key, value)
