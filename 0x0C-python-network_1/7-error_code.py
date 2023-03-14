#!/usr/bin/python3
"""header.py"""


import requests
import sys

if __name__ == "__main__":
    print(requests.get(sys.argv[1]).status_code)
