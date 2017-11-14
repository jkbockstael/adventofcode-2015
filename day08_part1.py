# Advent of Code 2015 - Day 8 - Matchsticks
# http://adventofcode.com/2015/day/8

import sys

# Main
print(sum([len(line.strip()) - len(eval(line)) for line in sys.stdin]))
