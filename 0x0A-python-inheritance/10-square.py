#!/usr/bin/python3
"""Defines the Square class, a subclass of Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """new sub class"""
    def __init__(self, size):
        """initialize data"""
        self.size = super().integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        name = str(Rectangle.__name__)
        s = str(self.size)
        lis = ["["] + [name] + ["] "] + [s] + ["/"] + [s]
        return "".join(lis)
