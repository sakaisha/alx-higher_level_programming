#!/usr/bin/python3
"""Defines the Rectangle class, a subclass of BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """new sub class"""
    def __init__(self, width, height):
        """initilialize the data"""
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
