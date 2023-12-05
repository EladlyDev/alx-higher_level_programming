#!/usr/bin/python3
""" 7. Load, add, save """

import sys
import json
to_json = __import__("5-save_to_json_file").save_to_json_file
from_json = __import__("6-load_from_json_file").load_from_json_file

# create the file if it doesn't exist, and if it does do nothing
with open("add_item.json", "a") as f:
    pass

with open("add_item.json", "r+", encoding="utf-8") as f:
    try:
        data = json.load(f)
    except json.decoder.JSONDecodeError:
        data = []

for item in sys.argv[1:]:
    data.append(item)
    pass

to_json(data, "add_item.json")
