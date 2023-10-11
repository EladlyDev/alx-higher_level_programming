#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        for key in sorted(list(a_dictionary.keys())):
            print("{0}: {1}".format(key, a_dictionary[key]))
