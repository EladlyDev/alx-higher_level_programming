#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        uniq = set(my_list)
        result = 0
        for x in uniq:
            result += x
        return result
    return 0
