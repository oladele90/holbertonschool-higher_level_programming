#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """Defines a class called rectangle"""

    def __init__(self, width=0, height=0):
        """initializes variable"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle"""

        return self.__height * self.__width

    def perimiter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.height) * 2
