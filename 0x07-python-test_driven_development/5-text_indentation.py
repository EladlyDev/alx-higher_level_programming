#!/usr/bin/python3
""" This module contains the ``text_indentation`` function """


def text_indentation(text):
    """ adds 2 newlines after any of these [".", ":", "?"] """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for c in text:
        print(c, end="")
        if c in ".?:":
            print("\n")
    pass
