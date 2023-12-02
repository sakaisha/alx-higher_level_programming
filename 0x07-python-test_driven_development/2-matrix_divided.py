#!/usr/bin/python3

"""Module: matrix_operations

   This module provides functions for matrix operations.

   Functions:
   - calculate_sum(a, b): Calculate the sum of two integers.
   - check_matrix(matrix): Check matrix validity.
   - matrix_divided(matrix, div): Divide matrix elements by a number.
"""

def calculate_sum(a, b):
    """Calculate sum of two integers
    Args:
    a: The first parameter
    b: The second parameter
    Returns: sum of 2 parameters
    """
    return a + b


def check_matrix(matrix):
    """Check the matrix if its rows have same size
    and check element must be integer or float type
    """
    temp = 0
    for row in matrix:
        for col in row:
            if type(col) not in (int, float):
                raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
        if temp == 0:
            temp = len(row)
        elif temp != len(row):
            raise TypeError("Each row of the matrix must have the same size")


def matrix_divided(matrix, div):
    """Return new matrix that each element will be
    divided by given div
    """
    try:
        check_matrix(matrix)
    except Exception as e:
        raise e
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(div) not in (int, float):
        raise TypeError("div must be a number")
    else:
        return [[round(x / div, 2) for x in row] for row in matrix]
