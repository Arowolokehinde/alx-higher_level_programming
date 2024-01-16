#!/usr/bin/pyhton3
"""
A class named Base
"""


class Base:
    """This is the private instance attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ The public instance attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
