#!/usr/bin/python3
def weight_average(my_list=[]):
    from functools import reduce
    if my_list:
        res_list = list(map(lambda x: x[0] * x[1], my_list))
        res = 0
        for x in res_list:
            res += x
        div = 0
        for tupe in my_list:
            div += tupe[1]
        return (res / div)
    return 0
