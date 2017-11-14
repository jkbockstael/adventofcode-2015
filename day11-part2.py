# Advent of Code 2015 - Day 11 - Corporate Policy - Part 2
# http://adventofcode.com/2015/day/11

import sys
from day11 import next_valid_password

# Main
print(next_valid_password(next_valid_password(sys.stdin.readline().strip())))
