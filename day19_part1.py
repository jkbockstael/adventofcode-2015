# Advent of Code 2015 - Day 19 - Medicine for Rudolph
# http://adventofcode.com/2015/day/19

import sys
import re

def parse_input(parse_replacement, lines):
    separator = ' => '
    replacements = {}
    for line in lines:
        if separator in line:
            source, replacement = parse_replacement(separator, line)
            if source in replacements:
                replacements[source].append(replacement)
            else:
                replacements[source] = [replacement]
            continue
        if line.rstrip() == '':
            continue
        molecule = line.rstrip()
    return replacements, molecule

def parse_replacement(separator, line):
    return line.rstrip().split(separator)
    
def split_molecule(molecule):
    return re.findall('[A-Z][a-z]*|e', molecule)

def replace(replacements, molecule):
    possible_outcomes = []
    atoms = split_molecule(molecule)
    for i in range(len(atoms)):
        atom = atoms[i]
        if atom in replacements:
            for replacement in replacements[atom]:
                outcome = atoms[:]
                outcome[i] = replacement
                joined = ''.join(outcome)
                if joined not in possible_outcomes:
                    possible_outcomes.append(joined)
    return possible_outcomes

# Main
if __name__ == '__main__':
    replacements, molecule = parse_input(parse_replacement, sys.stdin.readlines())
    possible_outcomes = replace(replacements, molecule)
    print(len(possible_outcomes))
