# Advent of Code 2015 - Day 4 - The Ideal Stocking Stuffer
# http://adventofcode.com/2015/day/4

import sys
import hashlib

# Find the lowest integer suffix that produces a MD5 hash starting with a given prefix
def find_lowest_suffix(required_prefix, key):
    suffix = 0
    while (not hashlib.md5(bytes(key + str(suffix), 'utf-8')).hexdigest().startswith(required_prefix)):
        suffix += 1
    return suffix

# Main
if __name__ == '__main__':
    key = sys.stdin.readline().strip()
    print(find_lowest_suffix('00000', key))
