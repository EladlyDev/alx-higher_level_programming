#!/usr/bin/python3
def no_c(my_string):
    list = [char for str in my_string for char in str if char not in "cC"]
    return "".join(list)
