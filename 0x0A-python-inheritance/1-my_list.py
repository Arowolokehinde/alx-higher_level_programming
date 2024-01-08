#!/usr/bin/python3
"""Function that inherits from the List"""


class MyList(list):
    """The function"""
    def print_sorted(self):
        """The sorted function"""
        list_sorted = sorted(self)
        print(list_sorted)
