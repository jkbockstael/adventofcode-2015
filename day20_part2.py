# Advent of Code 2015 - Day 20 - Infinite Elves and Infinite Houses - Part 2
# http://adventofcode.com/2015/day/20

import sys
from day20_part1 import divisors

def first_house(threshold):
    house = 1
    while sum([d for d in divisors(house) if house // d <= 50]) * 11 < threshold:
        house = house + 1
    return house

threshold = int(sys.stdin.readline().rstrip())
print(first_house(threshold))
