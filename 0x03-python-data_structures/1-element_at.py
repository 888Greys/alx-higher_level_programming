#!/bin/bash/python3
def find_index(number, my_list):
    if number in my_list:
        index = my_list.index(number)

        if index < 0 or index >= len(my_list):
            print("None")
        else:
            print(f"The number {number} is at index {index}")
    else:
        print(f"The number {number} is not in the list")
