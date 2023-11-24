#!/usr/bin/python3
""" This module contains the lookup function """


def lookup(obj):
    """ this function returns the list of available attributes and methods
    of an object """
    if issubclass(obj, object):
        return (dir(obj))
