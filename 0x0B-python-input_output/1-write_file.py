#!/usr/bin/python3
# 1-write_file.py
# Maira Wangui
"""
Module 1-write_file
Contains function that writes to text file and returns num chars written
"""


def write_file(filename="", text=""):
    """writes to text file and returns num chars written"""
    with open(filename, mode="w", encoding="utf-8") as fd:
        return (fd.write(text))
