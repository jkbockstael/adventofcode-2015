# Advent of Code 2015 - Day 15 - Science for Hungry People
# http://adventofcode.com/2015/day/15

import sys
import operator
import functools

def parse_input(text):
    return [parse_input_line(line.rstrip()) for line in text]

def parse_input_line(line):
    # Ignore the calories value altogether
    return list(map(lambda x: int(x.split(" ")[-1]), line.split(":")[1].split(",")))[:-1:]

def partitions():
    partitions = []
    for i in range(101):
        for j in range(101-i):
            for k in range(101-i-j):
                l = 100-i-j-k
                partitions.append([i,j,k,l])
    return partitions
    
def recipe_score(ingredients, quantities):
    weighted_ingredients = [list(map(lambda param: q*param, i)) for q,i in zip(quantities, ingredients)]
    properties = list(map(lambda a,b,c,d: a+b+c+d, *weighted_ingredients))
    no_negatives = list(map(lambda x: x if x>0 else 0, properties))
    return functools.reduce(operator.mul, no_negatives)

def best_recipe_score(ingredients):
    return max([recipe_score(ingredients, quantities) for quantities in partitions()])

# Main
ingredients = parse_input(sys.stdin.readlines())
print(best_recipe_score(ingredients))
