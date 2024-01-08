#!/usr/bin/python3
"""
function that raisee Exception
"""


class BaseGeometry:
    """The BaseGeomety class"""
    def area(self):
        """The public instance"""
        raise Exception("area() is not implemented")
