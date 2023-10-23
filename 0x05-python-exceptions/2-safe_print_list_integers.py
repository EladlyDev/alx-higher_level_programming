#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    len = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (TypeError, ValueError):
            continue
        else:
            len += 1
    print()
    return len
