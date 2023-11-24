#!/usr/bin/python3
""" this module contains the student class """


class Student:
    """ the Student class """

    def __init__(self, fn, ln, age):
        self.first_name = fn
        self.last_name = ln
        self.age = age

    def to_json(self):
        return self.__dict__
    pass
