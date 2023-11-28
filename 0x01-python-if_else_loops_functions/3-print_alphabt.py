#!/usr/bin/python3
#3-print_alphabt.py
#Maira Wangui

for letter in range(97, 123):
    if chr(letter) is not 'q' and chr(letter) is not 'e':
        print("{}".format(chr(letter)), end="")
