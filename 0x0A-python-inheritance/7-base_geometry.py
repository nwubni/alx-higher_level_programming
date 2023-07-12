#!/usr/bin/python3

"""Geometry Module"""


class BaseGeometry:
    """BaseGeometry Class"""
    pass

    def area(self):
        """Computes Shape's Area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
