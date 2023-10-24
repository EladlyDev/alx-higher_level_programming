#!/usr/bin/python3
"""6-square
Thi module defines a square by: (based on 5-square.py)
"""


class Square:
    """This is square class"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.size == 0:
            print()
            return

        [print() for i in range(0, self.__position[1])]
        for i in range(0, self.size):
            [print(" ", end="") for i in range(0, self.__position[0])]
            [print("#", end="") for i in range(0, self.__size)]
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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if (type(position) is not tuple or len(position) != 2 or
                type(position[0]) is not int or type(position[1])
                is not int or position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
