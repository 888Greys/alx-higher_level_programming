#!/usr/bin/python3
# Thise function replaces an element in the list
# at a specific position without modifying the original list

def new_in_list(my_list, idx, element):

    if idx < 0 or idx > (len(my_list) - 1):

        return (my_list)

    copy = [num for num in my_list]

    copy[idx] = element

    return (copy)
