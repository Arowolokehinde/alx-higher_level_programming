#!/usr/bin/python3
"""
contains the append file
"""


def append_write(filename="", text=""):
    """returns the number of characters appended to the string"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
