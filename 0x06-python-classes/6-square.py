#!/usr/bin/python3

"""
This module provides a simple Square class with methods to calculate the area
and print a square using hash (#) characters. The size attribute represents the
side length of the square, and the position attribute represents the offset of
the square's top-left corner.

Example:
    square = Square(3, (1, 2))
    square.my_print()
    # Output:
    #
    #
     ###
"""

class Square:
    """A class representing a square."""
    
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square instance.

        Args:
            size (int): The side length of the square.
            position (tuple): The position offset of the square's top-left corner.

        Raises:
            TypeError: If size is not an integer or float, or if position is not
                a tuple of two positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: The side length of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the side length of the square.

        Args:
            value (int): The side length of the square.

        Raises:
            TypeError: If value is not an integer or float.
            ValueError: If value is less than 0.
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """tuple: The position offset of the square's top-left corner."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position offset of the square's top-left corner.

        Args:
            value (tuple): The position offset as a tuple of two positive integers.

        Raises:
            TypeError: If value is not a tuple or has a length not equal to 2, or
                if the elements of the tuple are not integers, or if any element
                is less than 0.
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculate the area of the square."""
        return self.size * self.size

    def my_print(self):
        """Print the square using hash (#) characters."""
        if self.position[1] > 0 and self.size > 0:
            print("\n" * (self.position[1] - 1))
        for i in range(self.size):
            if self.position[0] > 0:
                print(" " * self.position[0], end="")
            print("#" * self.size, end="")
            print("")
        if self.size == 0:
            print("")

