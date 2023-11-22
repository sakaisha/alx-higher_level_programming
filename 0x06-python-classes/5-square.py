#!/usr/bin/python3
"""
This module defines the Square class.
"""

class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int): The size of the square (default is 0).
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method for the size of the square.

        Returns:
        - int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size of the square.

        Parameters:
        - value (int): The new size value.

        Raises:
        - ValueError: If the size is less than 0.
        - TypeError: If the size is not an integer.
        """
        if int(value) < 0:
            raise ValueError("size must be >= 0")
        elif value != int(value):
            raise TypeError("size must be an integer")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using '#' characters.

        If the size is 0, it prints an empty line.
        """
        for i in range(self.__size):
            print("#" * self.__size, end="")
            print("")
        if self.__size == 0:
            print("")
