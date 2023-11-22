#!/usr/bin/python3
"""
This module defines a Square class.

The Square class represents a square shape and is designed to store information about its size.

Example:
    square = Square(5)
    print(square.get_size())  # Output: 5
"""

class Square:
    """
    This class represents a square.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
