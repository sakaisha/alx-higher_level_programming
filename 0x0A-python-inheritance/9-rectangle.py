#!/usr/bin/python3
"""Module defining Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Subclass representing rectangles"""

    def __init__(self, width, height):
        """Initialize width and height attributes"""
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)

    def __str__(self):
        """Return string representation of the rectangle"""
        name = str(self.__class__.__name__)
        w = str(self.__width)
        h = str(self.__height)
        lis = ["["] + [name] + ["] "] + [w] + ["/"] + [h]
        return "".join(lis)

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.__height
