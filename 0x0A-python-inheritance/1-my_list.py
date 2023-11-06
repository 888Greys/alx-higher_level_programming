#!/usr/bin/python3
"""
Definition of the MyList class that inherits from the built-in list class
"""


class MyList(list):
    """
    A custom class named MyList that inherits all the functionality of a list.
    """
    def print_sorted(self):
        """
        Print the elements of the list in sorted order.
        """
        print(sorted(self))
