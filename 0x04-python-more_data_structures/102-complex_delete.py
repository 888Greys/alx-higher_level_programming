#!/usr/bin/python3
"""
Function that delete keys with specific vaalues
in the dictionary
"""


def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for value_dic in list_keys:
        if value == a_dictionary.get(value_dic):
            del a_dictionary[value_dic]

    return (a_dictionary)
# The code is actually working and its 3am
