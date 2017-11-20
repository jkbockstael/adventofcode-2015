# Advent of Code 2015 - Day 18 - Like a GIF For Your Yard
# http://adventofcode.com/2015/day/18

import sys

def parse_input(lines):
    return [[(lambda x: 1 if x == "#" else 0)(x) for x in line.rstrip()] for line in lines]

def count_neighbours(grid, line, column, state):
    size = len(grid)
    total = 0
    for x in range(line-1, line+2):
        for y in range(column-1, column+2):
            if (x == line and y == column) or x < 0 or x > size-1 or y < 0 or y > size-1:
                continue
            total += (1 if grid[x][y] == state else 0)
    return total

def cellular_rules(grid, line, column):
    cell = grid[line][column]
    if cell == 1 and count_neighbours(grid, line, column, 1) in [2,3]:
        return 1
    elif cell == 0 and count_neighbours(grid, line, column, 1) == 3:
        return 1
    else:
        return 0

def step(grid):
    size = len(grid)
    outcome = [[None for x in range(size)] for y in range(size)]
    for line in range(size):
        for column in range(size):
            outcome[line][column] = cellular_rules(grid, line, column)
    return outcome

def step_through(grid, steps):
    outcome = grid
    for s in range(steps):
        outcome = step(outcome)
    return outcome

def lights_on(grid):
    return sum([sum(line) for line in grid])

# Main
if __name__ == '__main__':
    start = parse_input(sys.stdin.readlines())
    print(lights_on(step_through(start, 100)))
