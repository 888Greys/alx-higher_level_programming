#!/usr/bin/python3
"""
a function that returns a tuple with
the length of a sr=tring and its
first character
"""


def multiple_returns(sentence):

    if sentence == "":

        return (0, None)

    return (len(sentence), sentence[0])
