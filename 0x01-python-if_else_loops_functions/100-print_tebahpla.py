#!/usr/bin/python3
lower = True
for i in reversed(range(65, 91)):
    out = i
    if lower:
        out = out + 32
        lower = False
    else:
        lower = True
    print("{:c}".format(out), end="")
