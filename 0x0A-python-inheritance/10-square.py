#!/usr/bin/python3
"""
Module to define a Square class inheriting from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A sub-class Square inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize Square object with size.
        """
        self.size = super().integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Return string representation of Square object.
        """
        name = str(Rectangle.__name__)
        s = str(self.size)
        lis = ["["] + [name] + ["] "] + [s] + ["/"] + [s]
        return "".join(lis)
