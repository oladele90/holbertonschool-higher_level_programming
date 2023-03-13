#!/usr/bin/python3
"""header.py"""


import urllib
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as resp:
        print(sys.argv[1])