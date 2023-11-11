#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        sub_matrix = map(lambda num: num**2, row)
        new_matrix.append(list(sub_matrix))
    return new_matrix
