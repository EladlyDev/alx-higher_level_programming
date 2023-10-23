#!/usr/bin/python3
def list_division(list1, list2, len):
    out = []
    for i in range(0, len):
        res = 0
        try:
            res = list1[i] / list2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            out.append(res)
    return (out)
