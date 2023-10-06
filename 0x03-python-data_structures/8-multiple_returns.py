#!/usr/bin/python3
def multiple_returns(str):
    strlen = len(str)
    if strlen == 0:
        out = 0, None
        return out
    out = strlen, str[0]
    return out
