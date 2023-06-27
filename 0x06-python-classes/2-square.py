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
