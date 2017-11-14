# Advent of Code 2015 - Day 1 - Not Quite Lisp
# http://adventofcode.com/2015/day/1

import sys

# Return the floor reached by following given directions
# Santa starts on the ground floor (0)
# - '(' in the directions makes him go up one floor
# - ')' in the directions makes him go down floor
def final_floor(directions):
    floor = 0
    for step in directions:
        if step == '(':
            floor += 1
        if step == ')':
            floor -= 1
    return floor

# Main
directions = sys.stdin.readline().strip()
print(final_floor(directions))
