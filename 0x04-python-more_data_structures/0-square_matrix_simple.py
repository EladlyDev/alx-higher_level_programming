#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        matrix = list(map(lambda row: [x*x for x in row],
                          [row for row in matrix]))
    return (matrix)
