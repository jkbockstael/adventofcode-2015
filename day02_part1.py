# Advent of Code 2015 - Day 2 - I Was Told There Would Be No Math
# http://adventofcode.com/2015/day/2

import sys

# Parse a box dimensions as a list
# Dimensions are given as a string formatted as LxHxW
def parse_dimensions(dimensions):
    return list(map(int, dimensions.strip().split('x')))

# Calculate the required wrapping for a given box dimensions
# This is the sum of each surface, plus the smallest of these surfaces as slack
def required_wrapping(dimensions):
    surfaces = calculate_surfaces(dimensions)
    return min(surfaces) + sum(map(lambda x: x * 2, surfaces))

# Calculate the three surfaces sizes for a box given its three edges lengths
def calculate_surfaces(dimensions):
    surfaces = []
    for edge in range(len(dimensions)):
        surfaces.append(dimensions[edge] * dimensions[edge - 1])
    return surfaces

# Main
total_wrapping = 0
for box in sys.stdin:
    total_wrapping += required_wrapping(parse_dimensions(box))
print(total_wrapping)
