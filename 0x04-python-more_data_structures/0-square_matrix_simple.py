#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    current_matrix = matrix.copy()

    for j in range(len(matrix)):
        current_matrix[j] = list(map(lambda x: x**2, matrix[j]))

    return (current_matrix)
