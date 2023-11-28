#!/usr/bin/python3
""" This file contains the class LockedClass """


class LockedClass():
    """ The LockedClass is a class that doesn't allowed any attributes that
    isn't equal to 'first_name'.
    """
    __slots__ = "first_name"
