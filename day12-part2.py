# Advent of Code 2015 - Day 12 - JSAbacusFramework.io - Part 2
# http://adventofcode.com/day/12

import sys
import json

# Sum all numbers from JSON data, except those in an object having a "red" value
def sum_all_numbers(data):
    if isinstance(data, int):
        return data
    elif isinstance(data, dict):
        if 'red' in data.values():
            return 0
        else:
            return sum([sum_all_numbers(data[key]) for key in data])
    elif isinstance(data, list):
        return sum([sum_all_numbers(value) for value in data])
    else:
        return 0

# Main
print(sum([sum_all_numbers(json.loads(line)) for line in sys.stdin]))
