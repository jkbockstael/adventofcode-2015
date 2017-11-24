# Advent of Code 2015 - Day 20 - Infinite Elves and Infinite Houses
# http://adventofcode.com/2015/day/20

import sys
from math import sqrt

def divisors(n):
    d = [x for x in range(1, int(sqrt(n)) + 1) if n % x == 0]
    d += [n // x for x in d if n != x**2]
    return d

def first_house(threshold):
    house = 1
    while sum(divisors(house)) * 10 < threshold:
        house = house + 1
    return house

# Main
if __name__ == '__main__':
    threshold = int(sys.stdin.readline().rstrip())
    print(first_house(threshold))
