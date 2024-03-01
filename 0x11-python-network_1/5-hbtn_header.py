#!/usr/bin/python3
""" sends a request to the URL and displays the value of the
variable X-Request-Id """
import requests
from sys import argv


if __name__ == "__main__":
    target = requests.get(argv[1]).headers.get("X-Request-Id")
    if target:
        print(target)
