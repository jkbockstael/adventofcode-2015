# Advent of Code 2015 - Day 16 - Aunt Sue - Part 2
# http://adventofcode.com/2015/day/16

from day16_part1 import *

def filter_aunt(key, value):
    if key in ['cats', 'trees']:
        return lambda aunt: aunt[key] is None or aunt[key] > value
    elif key in ['pomeranians', 'goldfish']:
        return lambda aunt: aunt[key] is None or aunt[key] < value
    else:
        return lambda aunt: aunt[key] in [None, value]

# Main
known = {'children':3, 'cats':7, 'samoyeds':2, 'pomeranians':3, 'akitas':0, 'vizslas':0, 'goldfish':5, 'trees':3, 'cars':2, 'perfumes':1}
print(aunt_number(filter_aunts(filter_aunt, known, parse_input(sys.stdin.readlines()))))
