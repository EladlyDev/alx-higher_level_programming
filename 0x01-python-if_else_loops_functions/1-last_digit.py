#!/usr/bin/python3
import random
number = random.randint(-1000, 10000)
ldig = int(repr(number)[-1])            # The last digit of the number variable
if ldig > 5:
    print(f"Last digit of {number} is {ldig} and is greater than 5")
elif ldig == 0:
    print(f"Last digit of {number} is {ldig} and is 0")
else:
    print(f"Last digit of {number} is {ldig} and is less than 6 and not 0")
