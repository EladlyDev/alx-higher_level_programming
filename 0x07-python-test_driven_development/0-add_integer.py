#!/usr/bin/python3
""" This module contains the test_integer function """


def add_integer(a, b=98):
    """ adds two integers and return the result """

    # validating the input
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    # in case of float
    a = int(a)
    b = int(b)

    return a + b
