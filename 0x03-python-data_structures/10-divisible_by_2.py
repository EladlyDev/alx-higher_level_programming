#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list = my_list.copy()
    for i in range(len(list)):
        if list[i] % 2 == 0:
            list[i] = True
        else:
            list[i] = False
    return list
