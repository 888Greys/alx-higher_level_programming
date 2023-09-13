#!/usr/bin/python3
"""
This script demonstrates the use of the integer_validator
method of the BaseGeometry class.

Usage:
    Execute this script to test the integer_validator
    method with various input values.
"""

# Import the BaseGeometry class from the '7-base_geometry' module
BaseGeometry = __import__('7-base_geometry').BaseGeometry

# Create an instance of the BaseGeometry class
bg = BaseGeometry()

# Test the integer_validator method with valid integers
bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    # Test the integer_validator method with a non-integer value
    bg.integer_validator("name", "John")
except Exception as e:
    # Handle the exception and print an error message
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    # Test the integer_validator method with an integer less than or equal to 0
    bg.integer_validator("age", 0)
except Exception as e:
    # Handle the exception and print an error message
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    # Test the integer_validator method with a negative integer
    bg.integer_validator("distance", -4)
except Exception as e:
    # Handle the exception and print an error message
    print("[{}] {}".format(e.__class__.__name__, e))
