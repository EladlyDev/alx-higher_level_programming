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

    type = r.headers.get('Content-Type')
    if not type or not type.startswith("application/json"):
        print("Not a valid JSON")
        exit(1)

    dict = r.json()

    if dict:
        print(f"[{dict['id']}] {dict['name']}")
    else:
        print("No result")
