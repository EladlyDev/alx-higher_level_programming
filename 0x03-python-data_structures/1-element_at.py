#!/usr/bin/python3
def element_at(my_list, idx):
    if idx > len(my_list) - 1 or idx < 0:
        return
    for i, num in enumerate(my_list):
        if i == idx:
            return num
