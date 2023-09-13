#!/usr/bin/python3
"""
MyList - A custom list class that inherits from the
built-in list class.
"""


class MyList(list):
    """
    MyList is a custom list class that extends the
    functionality of the built-in list class.

    It provides an additional method for printing
    the list in sorted order.
    """
    def print_sorted(self):
        """
        print_sorted(self) - Print the elements of
        the list in sorted order.

        Args:
            self: The MyList instance.

        Returns:
            None
        """
        print(sorted(self))
