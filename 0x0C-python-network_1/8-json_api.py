#!/usr/bin/python3
"""header.py"""


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        value = {'q': sys.argv[1]}
    if len(sys.argv) < 2:
        value = {'q': ""}
    req = requests.post("http://0.0.0.0:5000/search_user", value)
    try:
        val = req.json()
        if val.get('id') is None:
            print("No result")
        else:
            print("[{}] {}".format(val.get('id'), val.get('name')))
    except Exception:
        print("Not a valid JSON")
