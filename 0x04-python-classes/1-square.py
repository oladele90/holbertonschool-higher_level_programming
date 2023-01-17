#!/usr/bin/python3
"""Square"""


class Square:
    """Defines a class called Square"""

    def __init__(self, size=0):
        """Initialize Square, sets size, checks for size errors"""

        if type(size) not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
