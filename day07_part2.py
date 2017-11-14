# Advent of Code 2015 - Day 7 - Some Assembly Required - Part 2
# http://adventofcode.com/2015/day/7

import sys

from day07_part1 import *

# Main
circuit = parse_input(sys.stdin.readlines())
circuit['b'] = (GATE_INPUT, u16(solve_for(circuit, {}, 'a')), None)  # Solve the circuit for a, use that value as b
print(u16(solve_for(circuit, {}, 'a')))
