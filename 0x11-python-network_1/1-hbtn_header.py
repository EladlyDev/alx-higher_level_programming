#!/usr/bin/python3
""" sends a request to the URL and displays the value of the X-Request-Id
variable found in the header of the response."""
import urllib.request
from sys import argv

if __name__ == "__main__":
    request = urllib.request.Request(argv[1])

    with urllib.request.urlopen(request) as r:
        data = r.info().__dict__['_headers']
        for d in data:
            if d[0] == 'X-Request-Id':
                print(d[1])
                break
