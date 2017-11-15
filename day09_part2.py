# Advent of Code 2015 - Day 9 - All in a Single Night - Part 2
# http://adventofcode.com/2015/day/9

import sys

from day09_part1 import *

# Main
graph = parse_graph(sys.stdin.readlines())
print(max(tour_distances(graph)))
