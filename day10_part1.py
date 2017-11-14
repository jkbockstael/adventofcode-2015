# Advent of Code 2015 - Day 10 - Elves Look, Elves Say
# http://adventofcode.com/2015/day/10

import sys
import itertools

# Return the look-and-say string for a given input string
def look_and_say(string):
    return ''.join([str(len(list(values))) + value for value, values in itertools.groupby(string)])

# Apply a fonction N times to a given input
def repeat(func, arg, num):
    output = arg
    for i in range(num):
        output = func(output)
    return output

# Main
if __name__ == '__main__':
    print(len(repeat(look_and_say, sys.stdin.readline().strip(), 40)))
