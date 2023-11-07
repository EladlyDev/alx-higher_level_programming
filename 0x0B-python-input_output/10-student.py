#!/usr/bin/python3
""" this module contains the student class """


class Student:
    """ the Student class """

    def __init__(self, fn, ln, age):
        self.first_name = fn
        self.last_name = ln
        self.age = age

    def to_json(self, attr=None):
        if attr is not None:
            out = {item: self.__dict__[item] for item in attr if item in
                   self.__dict__}
            if len(out) < 1:
                return {}
            return out
        return self.__dict__
    pass
