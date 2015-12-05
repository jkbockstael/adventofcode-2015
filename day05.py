# Advent of Code 2015 - Day 5 - Doesn't He Have Intern-Elves For This?
# http://adventofcode.com/day/5

import sys

# Return True if a string is "nice":
# - contains at least three vowels AND
# - contains at least one letter that appears twice in a row AND
# - doesn't contain "ab", "cd", "pq", or "xy"
def is_nice(string):
    return has_three_vowels_or_more(string) and has_a_double(string) and not has_nasty_sequence(string)

# Return True if a string contains at least three vowels
def has_three_vowels_or_more(string):
    vowels = "aeiou"
    return len(list(filter(lambda x: x in vowels, string))) >= 3

# Returns True if a string contains a sequence of two same characters
def has_a_double(string):
    return any(map(lambda x: x * 2 in string, string))

# Return True if a string contains one of "ab", "cd", "pq", or "xy"
def has_nasty_sequence(string):
    nasty_strings = ["ab", "cd", "pq", "xy"]
    return any(map(lambda x: x in string, nasty_strings))

# Main
strings = sys.stdin
print(len(list(filter(is_nice, strings))))
