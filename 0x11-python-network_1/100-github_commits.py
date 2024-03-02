#!/usr/bin/python3
""" gets recent commits of the required repo """
import requests
from sys import argv


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    r = requests.get(url)

    type = r.headers.get('Content-Type')
    if not type or not type.startswith("application/json"):
        exit(1)

    i = 0
    data = r.json()
    for i in range(len(data)):
        if i == 10:
            break
        print(f"{data[i]['sha']}: {data[i]['commit']['author']['name']}")
