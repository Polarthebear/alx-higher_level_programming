#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_new = matrix.copy()

    for n in range(len(matrix)):
        matrix_new[n] = list(map(lambda x: x**2, matrix[n]))

    return (matrix_new)
