#!/usr/bin/python3
"""Module to define the Square class."""

class Square:
    """A class representing a square.

    Attributes:
        __size (int): The size of the square side.

    Methods:
        __init__(self, size=0): Initializes a new Square instance with a given size.
        area(self): Calculates and returns the area of the square.
    """

    def __init__(self, size=0):
        """Initialize the Square instance.

        Args:
            size (int): The size of the square side (default is 0).
        
        Raises:
            ValueError: If size is less than 0.
            TypeError: If size is not an integer.
        """
        self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")
        elif size != int(size):
            raise TypeError("size must be an integer")

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size
