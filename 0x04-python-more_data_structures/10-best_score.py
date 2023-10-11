#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max = list(a_dictionary.values())[0]
        max_key = list(a_dictionary.keys())[0]
        for key, val in a_dictionary.items():
            if val > max:
                max = val
                max_key = key
        return max_key
    return
