# An Advent of Code 2015 - Day 2 - I Was Told There Would Be No Math - Part 2
# http://adventofcode.com/day/2

import sys
import functools

# Parse a box dimensions as a list
# Dimensions are given as a string formatted as LxHxW
def parse_dimensions(dimensions):
    return list(map(int, dimensions.strip().split('x')))


# Calculate the required ribbon for a given box dimensions
# This is the smallest perimeter of the box's surfaces, plus the volume of the box
def required_ribbon(dimensions):
    return min(calculate_perimeters(dimensions)) + calculate_volume(dimensions)

# Calculate the perimeters of the surfaces for a given box dimensions
def calculate_perimeters(dimensions):
    perimeters = []
    for edge in range(len(dimensions)):
        perimeters.append(dimensions[edge] * 2 + dimensions[edge - 1] * 2)
    return perimeters

# Calculate the volume of a box
def calculate_volume(dimensions):
    return functools.reduce(lambda x, y: x * y, dimensions)

# Main
total_ribbon = 0
for box in sys.stdin:
    total_ribbon += required_ribbon(parse_dimensions(box))
print(total_ribbon)
