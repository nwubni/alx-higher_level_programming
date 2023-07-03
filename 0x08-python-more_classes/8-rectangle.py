#!/usr/bin/python3

""" Module that creates a rectangle class"""


class Rectangle:
    """Rectangle class
    Attr:
        number_of_instances (int): number of class instance
        print_symbol (str): rectangle print symbol
        width (int): rectangle width
        height (int): rectangle height
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Instantiats with optional parameter values """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """ Called when object is deleted """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

        if (self.__width == 0) or (self.__height == 0):
            return (0)

        return (2 * (self.__width + self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Method to compare the size of two rectangles """

        if not isinstance(rect_1, (Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, (Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")

        a1 = rect_1.area()
        a2 = rect_2.area()

        if a2 > a1:
            return (rect_2)

        return (rect_1)

    def __str__(self):
        """ Returns a string print of rectangle """

        output = ""

        if (self.__width == 0) or (self.__height == 0):
            return (output)

        self.print_symbol = str(self.print_symbol)

        for i in range(self.__height):
            output += (self.print_symbol * self.__width)

            if i < (self.__height - 1):
                output += "\n"

        return (output)

    def __repr__(self):
        """ Returns a string representing the class instance """

        return (f"Rectangle({self.__width}, {self.__height})")
