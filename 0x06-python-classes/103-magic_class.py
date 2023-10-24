#!/usr/bin/python3
"""
This is the same as MagicClass
it does somethings
"""
import math


class MagicClass():
    """
    This is description for the MagicClass so I can pass the checker
    """
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
