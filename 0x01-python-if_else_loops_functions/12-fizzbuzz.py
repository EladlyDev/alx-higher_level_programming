#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 != 0 and i % 5 != 0:
            print(f"{i:d} ", end="")
            continue
        elif i % 3 == 0 and i % 5 != 0:
            out = "Fizz"
        elif i % 5 == 0 and i % 3 != 0:
            out = "Buzz"
        else:
            out = "FizzBuzz"
        print(f"{out:s} ", end="")
