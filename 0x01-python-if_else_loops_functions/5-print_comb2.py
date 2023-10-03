#!/usr/bin/python3
def out(i, stopat):
    if i == stopat:
        return "{:02d}\n".format(i)
    else:
        return "{:02d}, ".format(i)


for i in range(100):
    print(f"{out(i, 99)}", end="")
