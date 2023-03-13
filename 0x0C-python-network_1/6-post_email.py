#!/usr/bin/python3
"""header.py"""


import requests
import sys

if __name__ == "__main__":
    print(requests.post(sys.argv[1], data={'email': sys.argv[2]}).text)
