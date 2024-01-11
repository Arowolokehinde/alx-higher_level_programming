#!/usr/bin/python3
"""
Module that defines the class student
"""


class Student:
    """class to create student class """
    def __init__(self, first_name, last_name, age):
        """ instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representration"""
        return self.__dict__.copy()
