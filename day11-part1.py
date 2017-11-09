# Advent of Code 2015 - Day 11 - Corporate Policy
# http://adventofcode.com/day/11

import sys
import itertools

# Return whether a password is valid per company policy
def is_valid_password(password):
    return not contains(password, 'iol') and has_straight_of_three(password) and has_two_pairs(password)

# Return true if a string contains an increasing straight of three letters
def has_straight_of_three(string):
    for i in range(len(string) - 2):
        if ord(string[i]) == ord(string[i + 1]) - 1 and ord(string[i]) == ord(string[i + 2]) - 2:
            return True
    return False

# Return true if a string contains at least a letter from a given set
def contains(string, letters):
    for letter in letters:
        if letter in string:
            return True
    return False

# Return true if a string contains at least two non-overlapping pairs of letters
def has_two_pairs(string):
    return len(list(filter(lambda x: x >= 2, [len(list(values)) for value, values in itertools.groupby(string)]))) >= 2

# Increment a password
def increment_password(password):
    if len(password) == 0:
        return 'a'
    if password[-1] == 'z':
        return increment_password(password[:-1]) + 'a'
    else:
        return password[:-1] + chr(ord(password[-1]) + 1)

# Return the next valid password, given the current one
def next_valid_password(current_password):
    current_password = increment_password(current_password)
    while not is_valid_password(current_password):
        current_password = increment_password(current_password)
    return current_password

# Main
if __name__ == '__main__':
    print(next_valid_password(sys.stdin.readline().strip()))
