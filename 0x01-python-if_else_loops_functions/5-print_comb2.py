#!/usr/bin/python3
def out(i, stopat):
    if i == stopat:
        return f"{i:02d}\n"
    else:
        return f"{i:02d}, "


for i in range(100):
    print(f"{out(i, 99)}", end="")
