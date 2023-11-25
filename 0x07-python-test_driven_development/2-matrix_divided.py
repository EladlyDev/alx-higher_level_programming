#!/usr/bin/python3
""" This module contains the matrix_divideed function """

MERR = 1
MLENERR = 2
DIVERR = 3
ZDIVERR = 4


def matrix_divided(matrix, div):
    """ Divides a ``matrix`` by ``div`` number """

    if type(div) not in [int, float]:
        err(DIVERR)
    elif div == 0:
        err(ZDIVERR)

    if (not matrix):
        return
    if type(matrix) is not list:
        err(MERR)

    out = []
    rlen = 0
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            err(MERR)
        for item in matrix[i]:
            if type(item) not in [float, int]:
                err(MERR)
        if i == 0:
            rlen = len(matrix[i])
        else:
            if (len(matrix[i]) != rlen):
                err(MLENERR)

        nitem = []
        for ele in matrix[i]:
            res = round(ele/div, 2)
            nitem.append(res)
        out.append(nitem)
    return out


def err(errno):
    """ raises a different erro based on the passed error number """

    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    err3 = "div must be a number"
    err4 = "division by zero"

    if errno == 1:
        raise TypeError(err1)
    elif errno == 2:
        raise TypeError(err2)
    elif errno == 3:
        raise TypeError(err3)
    elif errno == 4:
        raise ZeroDivisionError(err4)
