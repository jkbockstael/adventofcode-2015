# Advent of Code 2015 - Day 14 - Reindeer Olympics - Part 2
# http://adventofcode.com/2015/day/14

import sys
from day14_part1 import *

# Calculate the accumulated points gained along the race
def points_gained(reindeers, time):
    points = [0] * len(reindeers)
    for second in range(1, time + 1):
        positions = distances_traveled(reindeers, second)
        leading_position = max(positions)
        # Each reindeer in the leading position gets a point
        for i in range(len(positions)):
            if positions[i] == leading_position:
                points[i] += 1
    return points
        
# Main
print(max(points_gained(parse_reindeers(sys.stdin.readlines()), 2503)))
