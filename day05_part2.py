# Advent of Code 2015 - Day 5 - Doesn't He Have Intern-Elves For This? - Part 2
# http://adventofcode.com/2015/day/5

import sys

# Return True if a string is "nice":
# - contains a two-characters substring that appears twice
# - contains one letter that appears twice with exactly one letter in between
def is_nice(string):
    return has_double_pair(string) and has_pair_with_insert(string)

# Return True if a string contains a two-characters substring that appears twice
def has_double_pair(string):
    for substring in substrings(string, 2):
        first_position = string.find(substring)
        if first_position != -1 and string.find(substring, first_position + 2) != -1:
            return True
    return False

# Return True if a string contains one letter that appears twice with exactly one letter in between
def has_pair_with_insert(string):
    return any(map(lambda x: x[0] == x[-1], substrings(string, 3)))

# Return a list of substrings of a given length
def substrings(string, length):
    output = []
    for i in range(len(string) - (length - 1)):
        output.append(string[i:i+length])
    return output

# Main
strings = sys.stdin
print(len(list(filter(is_nice, strings))))
