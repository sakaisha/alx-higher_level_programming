#!/usr/bin/python3
"""Python module containing the Rectangle subclass."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """New sub class"""
    def __init__(self, width, height):
        """Initialize the data"""
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
