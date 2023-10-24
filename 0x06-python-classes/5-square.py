#!/usr/bin/python3
"""5-square
Thi module defines a square by: (based on 4-square.py)
"""


class Square:
    """This is square class"""
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if (self.size == 0):
            print()
        for i in range(0, self.size):
            for j in range(0, self.size):
                print("#", end="")
            print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
