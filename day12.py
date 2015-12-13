# Advent of Code 2015 - Day 12 - JSAbacusFramework.io
# http://adventofcode.com/day/12

import sys
import re

# Sum all numbers from JSON data
def sum_all_numbers(json_data):
    return sum(list(map(int, re.findall(r'-?\d+', json_data))))

# Main
print(sum([sum_all_numbers(line) for line in sys.stdin]))
