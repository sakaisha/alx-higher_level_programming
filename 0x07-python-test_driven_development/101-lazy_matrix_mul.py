#!/usr/bin/python3
import numpy as np

"""check the matrix
Args:
m: matrix
Returns: True/ False"""

def check_matrix(matrix, name):
    """check the matrix and return True/ False
    """
    if type(matrix) is not list:
        raise TypeError("{} must be a list".format(name))
    if matrix == []:
        raise ValueError("{} can't be empty".format(name))
    if matrix == [[]]:
        raise ValueError("{} must be a list of lists".format(name))

    temp = 0
    for sub_matrix in matrix:
        if type(sub_matrix) is not list:
            raise TypeError("{} must be a list of lists".format(name))
        if temp == 0:
            temp = len(sub_matrix)
        elif temp == len(sub_matrix):
            temp = sub_matrix
        else:
            raise TypeError("each row of {} must should be of the same size".format(name))
        for num in sub_matrix:
            if type(num) is not int and type(num) is not float:
                raise TypeError("{} should contain only integers or floats".format(name))



"""production of 2 matrices
Args:
m_a: first matrix
m_b: second matrix
Returns: new matrix"""

def lazy_matrix_mul(m_a, m_b):
    """print paragraph and give space after ".?:"
    """
    check_matrix(m_a, "m_a")
    check_matrix(m_b, "m_b")
    A = np.array(m_a)
    B = np.array(m_b)
    C = np.array(A.dot(B))
    D = [list(x) for x in C]
    return D
