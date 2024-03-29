#!/usr/bin/python3
# 4-from_json_string.py
# Maira Wangui
"""
Module 4-from_json_string
Contains function that returns python data structure from JSON string
"""


def from_json_string(my_str):
    """
    Returns python data structure from JSON string
    """
    import json

    return (json.loads(my_str))
