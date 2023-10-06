#!/usr/bin/python3
def atleastwo(list=[]):
    listlen = len(list)
    if listlen == 1:
        list.append(0)
    elif listlen == 0:
        list = [0, 0]
    return list


def add_tuple(tuple_a=(), tuple_b=()):
    list_a = atleastwo(list(tuple_a))
    list_b = atleastwo(list(tuple_b))
    # the calculations
    list_a[0] = list_a[0] + list_b[0]
    list_a[1] = list_a[1] + list_b[1]
    return(tuple(list_a))
