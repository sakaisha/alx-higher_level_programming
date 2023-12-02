#!/usr/bin/python3

"""Module: square_printer

This module defines a function to print a square filled with "#".

Functions:
- print_square(size): Prints a square of "#" with the specified size.

Usage:
print_square(5)
"""

def print_square(size):
    """Print a square of "#" characters with the given size.
    
    Args:
    size (int): The size of the square.

    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            print("#" * size)
