# Advent of Code 2015 - Day 13 - Knights of the Dinner Table
# http://adventofcode.com/day/13

import sys
import itertools

# Parse the guest list as a map
def parse_guest_list(guest_list):
    guests = {}
    for line in guest_list:
        tokens = line.split(' ')
        guest = tokens[0]
        other_guest = tokens[10][:-2]
        happiness_value = int(tokens[3]) * (-1 if tokens[2] == 'lose' else 1)
        if guest not in guests:
            guests[guest] = {}
        guests[guest][other_guest] = happiness_value
    return guests

# Return the total happiness for the best seating arrangement
def best_seating_outcome(guests):
    return max([sum(happiness(seating, guests)) for seating in itertools.permutations(guests)])

# Calculate the happiness value for each guest in a seating
def happiness(seating, guests):
    outcome = []
    for i in range(len(seating)):
        guest = seating[i]
        previous_guest = seating[i - 1]
        next_guest = seating[(i + 1) % len(seating)]
        outcome.append(guests[guest][previous_guest] + guests[guest][next_guest])
    return outcome
        
# Main
if __name__ == '__main__':
    print(best_seating_outcome(parse_guest_list(sys.stdin.readlines())))
