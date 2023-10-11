#!/usr/bin/python3
def roman_to_int(roman):
    roman_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
                 "M": 1000, "non": -1}
    if roman and type(roman) == str:
        roman = [x for x in roman if x in list(roman_dic.keys())]
        result = 0
        last = "non"
        for current in reversed(roman):
            if roman_dic[current] < roman_dic[last]:
                result -= roman_dic[current]
            else:
                result += roman_dic[current]
            last = current
        return result
    return 0
