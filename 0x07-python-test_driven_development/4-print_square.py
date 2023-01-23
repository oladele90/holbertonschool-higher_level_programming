#!/usr/bin/python3
def print_square(size):
    char = "#"
    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(int(size)):
        for i in range(int(size)):
            print("{}".format(char), end="")
        if x < size:
            print()
