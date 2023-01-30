#!/usr/bin/python3
"""append_write Module"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding="utf+8") as f:
        f.write(text)
        f.close()
