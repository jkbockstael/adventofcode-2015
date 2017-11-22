# Advent of Code 2015 - Day 19 - Medicine for Rudolph - Part 2
# http://adventofcode.com/2015/day/19

from day19_part1 import *
from collections import Counter

# We don't actually care *what* the steps are, just how many there are
def transformation_length(source):
    atoms = split_molecule(source)
    count = Counter(atoms)
    return len(atoms) - count['Ar'] - count['Rn'] - count['Y']*2 -1

# Main
_, molecule = parse_input(parse_replacement, sys.stdin.readlines())
print(transformation_length(molecule))
