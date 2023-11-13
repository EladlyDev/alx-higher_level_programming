#!/usr/bin/python3
""" Contains the rectangle class  that inherits from the Base class"""
from models.base import Base


class Rectangle(Base):
    """ the Rectangle class inherits from the Base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ this method is used to initialize the new instances """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ This is a getter for the width attr """
        return self.__width

    @width.setter
    def width(self, val):
        """ This is a setter for the width attr, it validates the val first """
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """ This is a getter for the height attr """
        return self.__height

    @height.setter
    def height(self, val):
        """ This is a setter for the height attr, it validates the val first"""
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """ This is a getter for the x attr """
        return self.__x

    @x.setter
    def x(self, val):
        """ This is a setter for the x attr, it validates the val first """
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """ This is a getter for the y attr """
        return self.__y

    @y.setter
    def y(self, val):
        """ This is a setter for the y attr, it validates the val first """
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """ This returns the area of the rectange/instance """
        return self.width * self.height

    def display(self):
        """ This method is used to display the rectangle """
        [print() for y in range(self.y)]
        for row in range(self.height):
            [print(" ", end='') for x in range(self.x)]
            [print("#", end='') for col in range(self.width)]
            print()

    def __str__(self):
        """ This returns a representation for the instance """
        return "[Rectangle] ({0}) {1}/{2} - {3}/{4}".format(self.id, self.x,
                                                            self.y, self.width,
                                                            self.height)

    def update(self, *args, **kwargs):
        """ This updates all instance's attrs all at once """
        keys = ['id', 'width', 'height', 'x', 'y']
        if len(args) >= 1:
            for i in range(len(args)):
                setattr(self, keys[i], args[i])
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """ This returns a dict rep for the instance, containing
        all the important values/attr """
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height,
                'width': self.width}
    pass
