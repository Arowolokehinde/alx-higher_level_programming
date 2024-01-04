#!/usr/bin/python3
"""a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:
    """a class that shows that width is a private instance attribute"""
    def __init__(self, width=0, height=0):
        """initializes the triangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the private instance attribute for height"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute for height"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute for width"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute for width"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError(" height must be >= 0")
        self.__height = value
