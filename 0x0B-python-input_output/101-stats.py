#!/usr/bin/python3
# 101-stats.py
# Maira Wangui

import sys

def print_size_and_codes(size, stat_codes):
    print("File size: {:d}".format(size))
    for k, v in sorted(stat_codes.items()):
        if v:
            print("{:s}: {:d}".format(k, v))

def parse_stdin_and_compute():
    size = 0
    lines = 0
    stat_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                  "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for line in sys.stdin:
            fields = list(map(str, line.strip().split(" ")))

            # Check if the last field is a valid integer
            try:
                size += int(fields[-1])
            except ValueError:
                print("Error: Invalid file size on line {}".format(lines + 1))
                continue

            if fields[-2] in stat_codes:
                stat_codes[fields[-2]] += 1
            lines += 1
            if lines % 10 == 0:
                print_size_and_codes(size, stat_codes)
    except KeyboardInterrupt:
        print_size_and_codes(size, stat_codes)
        raise

    print_size_and_codes(size, stat_codes)

parse_stdin_and_compute()
