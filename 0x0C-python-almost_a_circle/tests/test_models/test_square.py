#!/usr/bin/python3
""" Tests for class Square """
import unittest
from models.square import Square
import pep8


class TestSquare(unittest.TestCase):
    """ Tests for the Square class """

    def test_area(self):
        """
        Test the calculation of the area of a Square object.
        """
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_pep8(self):
        """
        Test PEP 8 compliance of the Square class implementation.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
