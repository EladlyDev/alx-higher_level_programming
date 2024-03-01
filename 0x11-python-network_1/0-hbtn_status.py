#!/usr/bin/python3
import urllib.request


request = urllib.request.Request("https://alx-intranet.hbtn.io/status")

with urllib.request.urlopen(request) as r:
    data = r.read()
    out = f"""Body response:
    - type: {type(data)}
    - content: {data}
    - utf8 content: {data.decode("utf-8")}"""
    print(out)
