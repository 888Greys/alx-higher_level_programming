#!/usr/bin/python3

if __name__ == "__main__":
    """Print the quotient, multiple, difference and sum of 5 and 10."""
    from calculator_1 import sub, add, mul, div

    a = 10
    b = 5

    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
