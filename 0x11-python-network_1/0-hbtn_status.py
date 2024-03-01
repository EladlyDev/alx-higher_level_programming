#!/usr/bin/python3
""" that fetches https://alx-intranet.hbtn.io/status """
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as r:
        data = r.read()
        out = f"""Body response:\n\t- type: {type(data)}\n\t- content: {data}\
\n\t- utf8 content: {data.decode("utf-8")}"""
        print(out)
