#!/usr/bin/python3
"""
contains the JSON format
"""
import json


def from_json_string(my_str):
    """returns the json format of my_str"""
    return json.loads(my_str)
