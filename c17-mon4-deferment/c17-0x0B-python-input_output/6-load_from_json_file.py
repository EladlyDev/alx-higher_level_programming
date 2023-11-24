#!/usr/bin/python3
""" 6. Create object from a JSON file """


def load_from_json_file(filename):
    """ creates an Object from a “JSON file” """
    with open(filename, encoding="utf-8") as f:
        import json
        return json.loads(f.read())
    pass
