#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response """
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    req = Request(argv[1])
    try:
        with urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as e:
        print(f"Error code: {e.code}")
