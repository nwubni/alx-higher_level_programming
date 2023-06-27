#!/usr/bin/python3
"""A class of square"""


class Square:
    """A class of square"""

    def __init__(self, size=0) -> None:
        """Initializes an instance of Square class
            Args:
                size (int): Size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """Retrieves the size of the square
            Return: Size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Updates the size of the square
            Args:
                value (int): New size of square
            Return: Nothing
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Calculates the area of the square based on the size"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints a square with dimension of size using the # symbol"""
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')

            print()
