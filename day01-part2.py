# Advent of Code 2015 - Day 1 - Not Quite Lisp - Part 2
# http://adventofcode.com/day/1

import sys


# Return the number of instructions to follow before reaching the basement (-1)
# Santa starts on the ground floor (0)
# - '(' in the directions makes him go up one floor
# - ')' in the directions makes him go down floor
def steps_to_enter_basement(directions):
    steps = 0
    floor = 0
    for step in directions:
        steps += 1
        if step == '(':
            floor += 1
        if step == ')':
            floor -= 1
        if floor == -1:
            return steps
    return None

# Main
directions = sys.stdin.readline().strip()
print(steps_to_enter_basement(directions))
