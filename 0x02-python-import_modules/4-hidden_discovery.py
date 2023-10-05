#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for definition in dir(hidden_4):
        if definition[0] + definition[1] != "__":
            print(definition)
