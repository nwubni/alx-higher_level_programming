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
        if not isinstance(value, (int)):
            raise TypeError(f"{name} must be an integer")

        if value == None or value <= 0:
            raise ValueError(f"{name} must be greater than 0")
