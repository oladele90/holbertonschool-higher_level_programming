#!/usr/bin/python3
"""header.py"""


import requests
import sys

if __name__ == "__main__":
    if requests.get(sys.argv[1]).status_code >= 400:
        print("Error code: {}".format(requests.get(sys.argv[1]).status_code))
    else:
        print(requests.get(sys.argv[1]).text)
