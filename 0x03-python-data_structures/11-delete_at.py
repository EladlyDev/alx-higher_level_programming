#!/usr/bin/python3
def delete_at(list=[], idx=0):
    listlen = len(list)
    if idx > listlen - 1 or idx < 0:
        return list
    del list[idx]
    return list
