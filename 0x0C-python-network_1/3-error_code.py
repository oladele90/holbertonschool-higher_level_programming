#!/usr/bin/python3
"""header.py"""


import urllib
import urllib.request
import urllib.parse
import urllib.error
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as resp:
            print(resp.read().decode('utf8'))
    except urllib.error.HTTPError as ec:
        print("Error code: {}".format(ec))