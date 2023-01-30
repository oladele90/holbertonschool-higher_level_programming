#!/usr/bin/python3
"""read_file module"""


def write_file(filename="", text=""):
    """writes a string to a text file"""

    with open(filename, 'r+' encoding="utf+8") as f:
        f.write(text)
        f.close()
