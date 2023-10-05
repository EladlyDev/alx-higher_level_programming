#!/usr/bin/python3
from sys import argv as av
if __name__ == "__main__":
    avlen = len(av)
    if avlen == 1:
        print("0 arguments.")
    elif avlen == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(avlen - 1))
    for i in range(1, len(av)):
        print("{}: {}".format(i, av[i]))
