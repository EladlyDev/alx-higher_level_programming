#!/usr/bin/python3
for fdig in range(10):
    for sdig in range(fdig + 1, 10):
        if (fdig == 8 and sdig == 9):
            print("{:d}{:d}".format(fdig, sdig))
        else:
            print("{:d}{:d}, ".format(fdig, sdig), end="")
