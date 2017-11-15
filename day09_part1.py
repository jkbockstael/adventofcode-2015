# Advent of Code 2015 - Day 9 - All in a Single Night
# http://adventofcode.com/2015/day/9

import sys
import itertools

# Parse the input and return a map
def parse_graph(distances):
    graph = {}
    for line in distances:
        edge, length = line.split(' = ')
        length = int(length)
        origin, destination = edge.split(' to ')
        graph[(origin, destination)] = length
        graph[(destination, origin)] = length
    return graph

# Compute tour distances through all the cities
# The problem input size is small enought to allow this rather inelegant brute force approach
def tour_distances(graph):
    tours = itertools.permutations(set([x for x, y in graph.keys()]))
    lengths = []
    for tour in tours:
        length = 0
        for i in range(len(tour) - 1):
            length += graph[(tour[i], tour[i + 1])]
        lengths.append(length)
    return lengths

# Main
if __name__ == '__main__':
    graph = parse_graph(sys.stdin.readlines())
    print(min(tour_distances(graph)))
