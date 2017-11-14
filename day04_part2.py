# Advent of Code 2015 - Day 4 - The Ideal Stocking Stuffer - Part 2
# http://adventofcode.com/2015/day/4

from day04_part1 import *

# Main
key = sys.stdin.readline().strip()
print(find_lowest_suffix('000000', key))
