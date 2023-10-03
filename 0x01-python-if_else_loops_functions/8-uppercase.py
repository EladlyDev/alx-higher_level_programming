#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        ascval = ord(str[i])
        if ascval >= 97 and ascval <= 122:
            ascval = ascval - 32
        if (i != len(str) - 1):
            print(f"{ascval:c}", end="")
        else:
            print(f"{ascval:c}")
