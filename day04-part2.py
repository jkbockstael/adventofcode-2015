# Advent of Code 2015 - Day 4 - The Ideal Stocking Stuffer - Part 2
# http://adventofcode.com/day/4

import sys
import hashlib

# Find the lowest integer suffix that produces a MD5 hash starting with six zeroes
def find_lowest_suffix(key):
    suffix = 0
    while (not hashlib.md5(bytes(key + str(suffix), 'utf-8')).hexdigest().startswith('000000')):
        suffix += 1
    return suffix

# Main
key = sys.stdin.readline().strip()
print(find_lowest_suffix(key))
