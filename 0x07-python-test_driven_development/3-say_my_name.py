#!/usr/bin/python
""" This module contains the say_my_name function """


def say_my_name(fn, ln=""):
    """ prints my name like: "My name is ``fn`` ``ln`` """

    if type(fn) is not str:
        raise TypeError("first_name must be a string")
    if type(ln) is not str:
        raise TypeError("last_name must be a string")

    fn = " " + fn if len(fn) > 0 else fn
    ln = " " + ln if len(ln) > 0 else ln

    print(f"My name is{fn}{ln}")
