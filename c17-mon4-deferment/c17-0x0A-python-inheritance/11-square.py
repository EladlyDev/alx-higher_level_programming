#!/usr/bin/python3
""" 7. Integer validator """


class BaseGeometry:
    """ This isn't an empty class """
    def area(self):
        return self._width * self._height

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """  inherits from Rectangle """
    def __init__(self, size):
        super().__init__(size, size)
        self._size = size

    def __str__(self):
        return f"[Square] {self._size}/{self._size}"
    pass
