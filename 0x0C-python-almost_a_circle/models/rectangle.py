#!/usr/bin/python3
""" Contains the rectangle class """
from models.base import Base


class Rectangle(Base):
    """ the Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        return self.width * self.height

    def display(self):
        [print() for y in range(self.y)]
        for row in range(self.height):
            [print(" ", end='') for x in range(self.x)]
            [print("#", end='') for col in range(self.width)]
            print()

    def __str__(self):
        return "[Rectangle] {0} {1}/{2} - {3}/{4}".format(self.id, self.x,
                                                          self.y, self.width,
                                                          self.height)

    def update(self, *args, **kwargs):
        id = None
        if len(args) >= 1:
            attr = [id, self.width, self.height, self.x, self.y]

            for i in range(len(args)):
                attr[i] = args[i]

            id, self.width, self.height, self.x, self.y = attr
            super().__init__(id)
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)
    pass
