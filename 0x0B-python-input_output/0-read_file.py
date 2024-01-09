#!/usr/bin/python3
"""
This contains the read_file Function
"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
