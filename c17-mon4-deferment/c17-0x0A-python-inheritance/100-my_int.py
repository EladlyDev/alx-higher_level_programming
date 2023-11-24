#!/usr/bin/python3
""" 12. My integer """


class MyInt(int):
    """ class MyInt that inherits from int """

    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val != other

    def __ne__(self, other):
        return self.val == other
