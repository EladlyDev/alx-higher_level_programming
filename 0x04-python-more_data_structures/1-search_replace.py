#!/usr/bin/python3
def search_replace(my_list, target, new):
    if my_list:
        my_list = list(map(lambda x: new if x == target else x, my_list))
    return my_list
