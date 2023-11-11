#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        squared_row = map(lambda num: num**2, row)
        squared_matrix.append(list(squared_row))
        return squared_matrix
