#!/usr/bin/python3
"""Defines a class MyInt that inherits from integer."""


class MyInt(int):
    """Invert int operators."""

    def __eq__(self, value):
        """Override == opeartor """
        return self.real != value

    def __ne__(self, value):
        """Override != operator with"""
        return self.real == value
