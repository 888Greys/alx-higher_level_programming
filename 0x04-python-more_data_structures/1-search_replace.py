#!/usr/bin/python3
def search_replace(my_list, search, replace):
    current_list = list(map(lambda y: replace if y == search else y, my_list))

    return (current_list)
