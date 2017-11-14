# Advent of Code 2015 - Day 13 - Knights of the Dinner Table - Part 2
# http://adventofcode.com/2015/day/13

from day13_part1 import *

# Add me to the guests list, as a neutral element
def add_me(guests):
    guest_names = guests.keys()
    guests['Me'] = {}
    for guest_name in guest_names:
        guests['Me'][guest_name] = 0
        guests[guest_name]['Me'] = 0
    return guests

# Main
guests = parse_guest_list(sys.stdin.readlines())
guests = add_me(guests)
print(best_seating_outcome(guests))
