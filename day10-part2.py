# Advent of Code 2015 - Day 10 - Elves Look, Elves Say - Part 2
# http://adventofcode.com/2015/day/10

import sys
from day10 import *

# Main
print(len(repeat(look_and_say, sys.stdin.readline().strip(), 50)))
