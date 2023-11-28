#!/usr/bin/python3
# 3-print_alphabt.py
# Maira Wangui

for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
