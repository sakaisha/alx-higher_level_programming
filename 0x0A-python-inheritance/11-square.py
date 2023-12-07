#!/usr/bin/python3
"""Module for Square class inheriting from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A new subclass representing a square"""
    def __init__(self, size):
        """
        Initialize Square class

        Args:
        - size: integer, size of the square
        """
        self.__size = super().integer_validator("size", size)
        super().__init__(size, size)
