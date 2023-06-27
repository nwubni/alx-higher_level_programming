#!/usr/bin/python3
"""A class of square"""


class Square:
    """A class of square"""

    def __init__(self, size=0, position=(0, 0)) -> None:
        """Initializes an instance of Square class
            Args:
                size (int): Size of the square
                position (tuple): Specifies position of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Retrieves the position of the square
            Return: Position tuple"""
        return self.__position

    @size.setter
    def position(self, value):
        """Updates the size of the square
            Args:
                value (int): New size of square
            Return: Nothing
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Calculates the area of the square based on the size"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints a square with dimension of size using the # symbol"""
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            print(
                " " * (self.__position[0] if self.__position[1] == 0 else self.__position[1]), end='')
            for j in range(self.__size):
                print("#", end='')

            print()
