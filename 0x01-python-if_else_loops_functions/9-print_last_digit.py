#!/usr/bin/python3
def print_last_digit(number):
    ldig = int(repr(number)[-1])
    print(f"{ldig:d}", end="")
    return ldig
