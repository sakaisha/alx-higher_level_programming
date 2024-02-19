#!/usr/bin/python3
"""Defines the Rectangle class, a subclass of BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """new sub class"""
    def __init__(self, width, height):
        """initialize the data"""
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)

    def __str__(self):
        """return str function"""
        name = str(self.__class__.__name__)
        w = str(self.__width)
        h = str(self.__height)
        lis = ["["] + [name] + ["] "] + [w] + ["/"] + [h]
        return "".join(lis)

    def area(self):
        """overwrite area function"""
        return self.__width * self.__height
