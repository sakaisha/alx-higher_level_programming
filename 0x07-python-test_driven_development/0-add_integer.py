#!/usr/bin/python3

"""This module provides a function to calculate the sum of two integers."""

def add_integer(a, b=98):
    """Calculate sum of two integers.

    Args:
        a (int or float): The first parameter.
        b (int or float): The second parameter. Default is 98.

    Returns:
        int: The sum of the two parameters.
    """
    # Check if a is an integer or float
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    # Check if b is an integer or float
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    # Return the sum of a and b
    else:
        return int(a) + int(b)
