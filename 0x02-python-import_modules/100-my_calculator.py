#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv as av


def getfunc(op):
    # getfunc: gets the suitable function for each operator and returns it.
    if op == "+":
        return add
    elif op == "-":
        return sub
    elif op == "/":
        return div
    elif op == "*":
        return mul


if __name__ == "__main__":
    avlen = len(av)
    if avlen != 4:
        print(f"Usage: {av[0]} <a> <operator> <b>")
        exit(1)
    ops = "+-/*"
    a = int(av[1])
    b = int(av[3])
    op = av[2]
    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    func = getfunc(op)
    print(f"{a} {op} {b} = {func(a, b)}")
