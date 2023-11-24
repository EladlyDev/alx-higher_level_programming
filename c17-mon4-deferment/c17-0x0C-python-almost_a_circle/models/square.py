#!/usr/bin/python3
""" This file contains the Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ The Square class inherates from the rectangles class """

    def __init__(self, size, x=0, y=0, id=None):
        """ used to initialize all the class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ this will return like a discreption for the instance/square """
        return "[Square] ({0}) {1}/{2} - {3}".format(self.id, self.x, self.y,
                                                     self.width)

    @property
    def size(self):
        """ this returns the size of the square, which is its width/height"""
        return self.width

    @size.setter
    def size(self, val):
        """ This is a setter for the size attr, it's update the width/height"""
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """ this updates the instance's attributes, all at once """
        keys = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, keys[i], args[i])
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """ this returns a dictionary representation to the instance """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
    pass
