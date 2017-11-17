# Advent of Code 2015 - Day 16 - Aunt Sue
# http://adventofcode.com/2015/day/16

import sys

class Aunt(dict):
    def __missing__(self, key):
        return None

def parse_input(text):
    def parse_line(line):
        aunt = Aunt()
        aunt['id'] = int(line.split(':')[0].split(' ')[-1])
        items = map(lambda x: x.split(' '),' '.join(line.split(': ')[1:]).split(', '))
        for item, count in items:
            aunt[item] = int(count)
        return aunt
    return [parse_line(line) for line in text]
        

def filter_aunt(key, value):
    return lambda aunt: aunt[key] in [None, value]

def filter_aunts(filter_function, known, aunts):
    for key in known:
        aunts = list(filter(filter_function(key, known[key]), aunts))
    return aunts[0];

def aunt_number(aunt):
    return aunt['id']

# Main
if __name__ == '__main__':
    known = {'children':3, 'cats':7, 'samoyeds':2, 'pomeranians':3, 'akitas':0, 'vizslas':0, 'goldfish':5, 'trees':3, 'cars':2, 'perfumes':1}
    print(aunt_number(filter_aunts(filter_aunt, known, parse_input(sys.stdin.readlines()))))
