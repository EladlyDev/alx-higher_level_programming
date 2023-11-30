#!/usr/bin/python3
""" This module contains the ``text_indentation`` function """


def text_indentation(text):
    """ adds 2 newlines after any of these [".", ":", "?"] """
    nline = False

    if type(text) is not str:
        raise TypeError("text must be a string")

    for c in text:
        if c in ".?:":
            print(c, end="")
            print("\n")
            nline = True
            continue
        if nline and c == " ":
            nline = False
            continue

        print(c, end="")
        nline = False
    pass
