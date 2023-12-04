#!/usr/bin/python3
""" 7. Integer validator """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """  inherits from Rectangle """
    def __init__(self, size):
        super().__init__(size, size)
        self._size = size

    def __str__(self):
        return f"[Square] {self._size}/{self._size}"
    pass
