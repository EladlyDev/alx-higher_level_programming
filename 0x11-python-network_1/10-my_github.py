#!/usr/bin/python3
""" displays yoeur id using github api """
import requests
from sys import argv


if __name__ == "__main__":
    header = {"Authorization": f"Bearer {argv[2]}"}
    r = requests.get("https://api.github.com/user", headers=header)

    dict = r.json()
    if 'id' in dict:
        print(dict['id'])
    else:
        print("None")
