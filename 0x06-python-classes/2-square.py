#!/usr/bin/python3
"""
This module defines a Square class.

A Square represents a geometric shape with equal sides.

Attributes:
    size (int): The size of the square's sides.

Methods:
    __init__(self, size=0): Initializes a new instance of the Square class.

Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than 0.
"""

class Square:
    """
    This class represents a square.

    Attributes:
        size (int): The size of the square's sides.

    Methods:
        __init__(self, size=0): Initializes a new instance of the Square class.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square's sides.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size
        if size != int(size):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

