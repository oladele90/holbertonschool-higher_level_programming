#!/usr/bin/python3
"""Square"""


class Square:
    """Defines a class called Square"""

    def __init__(self, size=0):
        """initializes variable"""
        self.__size = size

    @property
    def size(self):
        """Get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns area of square"""

        return self.__size * self.__size

    def my_print(self):
        """Prints the square"""
        for i in range(0, self.__size):
            if i > 0:
                print()
            for j in range(0, self.__size):
                print("#", end="")
        print()
