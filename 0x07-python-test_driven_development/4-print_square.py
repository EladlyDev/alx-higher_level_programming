#!/usr/bin/python3
""" This module contains the ``print_square`` function """


def print_square(size):
    """ Prints a square with the size of ``size`` """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for x in range(size)]
        print("")
