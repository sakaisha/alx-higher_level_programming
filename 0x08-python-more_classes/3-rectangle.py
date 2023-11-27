#!/usr/bin/python3
"""Class rectangle 4"""


class Rectangle:
    """A class representing a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with specified width and height."""
        self.height = height
        self.width = width

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with type and value checks."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with type and value checks."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """Return a string representation of the rectangle."""
        lis = []
        for i in range(self.__height):
            if self.__width > 0:
                lis += ["#" * self.__width]
        return "\n".join(lis)

