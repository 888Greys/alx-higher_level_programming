#!/usr/bin/python3
"""
This script imports a custom module 'is_same_class'
and uses the 'is_same_class' function
to check if a variable 'a' is an instance of certain
classes ('int', 'float', and 'object').
It then prints messages based on the results of these checks.
"""


is_same_class = __import__('2-is_same_class').is_same_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))
