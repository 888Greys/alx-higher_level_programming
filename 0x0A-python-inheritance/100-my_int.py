#!/usr/bin/python3
""" class MyInt that inherits from integer """


class MyInt(int):

    def __eq__(self, other):
        """ equals change """
        return super().__ne__(other)

    def __ne__(self, other):
        """ not equals """
        return super().__eq__(other)
