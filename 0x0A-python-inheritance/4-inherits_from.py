#!/usr/bin/python3
"""
 function that returns True if the object is an instance
"""


def inherits_from(obj, a_class):
    """ returns true else false if otherwise"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
