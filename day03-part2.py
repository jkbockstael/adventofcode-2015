# Advent of Code 2015 - Day 3 - Perfectly Spherical Houses in a Vacuum - Part 2
# http://adventofcode.com/day/3

import sys

# Return a list of visited houses given a moves list
# The starting position counts as visited
# This version uses two actors: Santa and a robot, moving each one after the other
# This means that, starting with zero, even-numbered steps will move Santa and odd-numbered steps will move the robot
def visited_positions_with_robot(directions):
    position_santa = (0, 0)
    position_robot = (0, 0)
    visited = [(0, 0)]
    for step_number in range(len(directions)):
        if step_number % 2 == 0:
            x, y = position_santa
        else:
            x, y = position_robot
        if directions[step_number] == '<':
            x -= 1
        elif directions[step_number] == '>':
            x += 1
        elif directions[step_number] == 'v':
            y -= 1
        elif directions[step_number] == '^':
            y += 1
        position = (x, y)
        if position not in visited:
            visited.append(position)
        if step_number % 2 == 0:
            position_santa = position
        else:
            position_robot = position
    return visited

# Main
directions = sys.stdin.readline().strip()
print(len(visited_positions_with_robot(directions)))
