#!/usr/bin/python3

if __name__ == "__main__":
    """The code that prints out the sum of one and three"""
    from add_0 import add

    a = 2
    b = 1
    print("{} + {} = {}".format(a, b, add(a, b, add(a, b)))
