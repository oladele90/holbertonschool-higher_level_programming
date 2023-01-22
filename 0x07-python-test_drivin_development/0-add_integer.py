#!/usr/bin/python3
"""add_integer module"""

def add_integer(a, b=98):
    """Adds two integers"""
    if a is not int or a is not float:
        raise TypeError("a must be an integer")
    if b is not int or b is not float:
        raist TypeError("b must be an integer")
    return int(a) + int(b)
