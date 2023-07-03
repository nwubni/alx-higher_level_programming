#!/usr/bin/python3

""" Module that creates a rectangle class"""


class Rectangle:
    """Rectangle class
    Attr:
        width (int): rectangle width
        height (int): rectangle height
    """

    def __init__(self, width=0, height=0):
        """ Instantiats with optional parameter values """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves rectangle width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets rectangle width to value"""

        if not isinstance(value, (int)):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Retrieves rectangle height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets rectangle height to value"""

        if not isinstance(value, (int)):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ Calculates area of rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Calculates perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)

        return (2 * (self.__width * self.__height))
