# Advent of Code 2015 - Day 18 - Like a GIF For Your Yard - Part 2
# http://adventofcode.com/2015/day/18

from day18_part1 import *

def step_through(grid, steps):
    outcome = grid
    size = len(grid)
    for s in range(steps):
        outcome = step(outcome)
        # corners stay on no matter what
        outcome[0][0] = 1
        outcome[0][size-1] = 1
        outcome[size-1][size-1] = 1
        outcome[size-1][0] = 1
    return outcome

start = parse_input(sys.stdin.readlines())
print(lights_on(step_through(start, 100)))
