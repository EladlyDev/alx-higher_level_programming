#!/usr/bin/python3
""" This module contains a class MyList that adds to the list class """


class MyList (list):
    """ This class builds upon the list class """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
