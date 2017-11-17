# Advent of Code 2015 - Day 17 - No Such Thing as Too Much - Part 2
# http://adventofcode.com/2015/day/17

import sys
from day17_part1 import *

def smallest_only(combinations):
    smallest = min([len(comb) for comb in combinations])
    return [comb for comb in combinations if len(comb) == smallest]

# Main
containers = parse_input(sys.stdin.readlines())
print(len(smallest_only(combinations(containers, 150))))
