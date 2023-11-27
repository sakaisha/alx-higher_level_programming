#!/usr/bin/python3
"""Class reccc module"""


class Rectangle:
    """Define Rectangle class."""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize class attributes."""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
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
        """Set the width of the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
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

    def __repr__(self):
        """Return a string representation for reproduction."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Delete an instance of the rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
