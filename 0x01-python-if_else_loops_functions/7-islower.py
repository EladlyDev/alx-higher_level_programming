#!/usr/bin/python3
def islower(c):
    ascval = ord(c)
    if ascval >= 97 and ascval <= 122:
        return True
    elif ascval >= 65 and ascval <= 90:
        return False
