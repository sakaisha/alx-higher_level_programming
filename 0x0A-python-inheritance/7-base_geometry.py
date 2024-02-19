#!/usr/bin/python3
"""Defines the BaseGeometry class."""


class BaseGeometry:
    """create a new class"""
    def area(self):
        """function to calculate area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validating the data"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            return value
