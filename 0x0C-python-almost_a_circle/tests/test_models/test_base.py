#!/usr/bin/python3
""" Tests for class Base """
import unittest
from models.base import Base
import pep8


class TestBase(unittest.TestCase):
    """ Tests for the Base class """

    def test_id(self):
        """
        Test the generation of unique IDs by the Base class.
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)
        with self.assertRaises(TypeError):
            Base(5, 6)

    def test_pep8(self):
        """
        Test PEP 8 compliance of the Base class implementation.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
