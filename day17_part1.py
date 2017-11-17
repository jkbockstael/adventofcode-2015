# Advent of Code 2015 - Day 17 - No Such Thing as Too Much
# http://adventofcode.com/2015/day/17

import sys
import itertools

def parse_input(lines):
    return [int(line) for line in lines]

def combinations(containers, total):
    combs = []
    for count in range(len(containers)):
        combs += [comb for comb in itertools.combinations(containers, count) if sum(comb) == 150]
    return combs

# Main
if __name__ == '__main__':
    containers = parse_input(sys.stdin.readlines())
    print(len(combinations(containers, 150)))
