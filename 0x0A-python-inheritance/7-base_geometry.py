#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


class BaseGeometry:
    """The BaseGeomety class"""
    def area(self):
        """The public instance"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ value validator"""
        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError("{:s}<name> must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s}<name> must be greater than 0".format(name))
