#!/usr/bin/python3
""" sends a POST request to the passed URL with the letter as a parameter """
import requests
from sys import argv


if __name__ == "__main__":
    url = ""
    if len(argv) >= 2:
        url = argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user",
                      data={'q': url})
    if r.headers['Content-Type'] == "application/json":
        dict = r.json()
    else:
        print("Not a valid JSON")
        exit
    if dict:
        print(f"[{dict['id']}] {dict['name']}")
    else:
        print("No result")
