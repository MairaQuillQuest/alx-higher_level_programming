#!/usr/bin/python3
# 3-to_json_string.py
# Maira Wangui
"""
Module 3-to_json_string
Contains function that returns JSON representation of obj (string)
"""


def to_json_string(my_obj):
    """
    Returns JSON representation of obj (string)
    """
    import json

    return (json.dumps(my_obj))
