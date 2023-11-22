#!/usr/bin/python3
"""
This module defines the Square class.

A Square is a geometric shape with a specified size.

Attributes:
    size (int): The size of the square.

Methods:
    __init__: Initializes a new instance of the Square class.
    area: Calculates the area of the square.

"""

class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """Initializes a new square with a specified size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
