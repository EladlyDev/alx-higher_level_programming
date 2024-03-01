#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status """
import requests


if __name__ == "__main__":
    content = requests.get("https://alx-intranet.hbtn.io/status").text
    out = f"""Body response:\n\t- type: {type(content)}\n\t-\
 content: {content}"""
    print(out)
