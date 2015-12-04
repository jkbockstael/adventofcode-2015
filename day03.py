# An Advent of Code 2015 - Day 3 - Perfectly Spherical Houses in a Vacuum
# http://adventofcode.com/day/3

import sys

# Return a list of visited houses given a moves list
# The starting position counts as visited
def visited_positions(directions):
    position = (0, 0)
    visited = [(0, 0)]
    for step in directions:
        x, y = position
        if step == '<':
            x -= 1
        elif step == '>':
            x += 1
        elif step == 'v':
            y -= 1
        elif step == '^':
            y += 1
        position = (x, y)
        if position not in visited:
            visited.append(position)
    return visited

# Main
directions = sys.stdin.readline().strip()
print(len(visited_positions(directions)))
