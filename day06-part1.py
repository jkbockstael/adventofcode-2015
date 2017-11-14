# Advent of Code 2015 - Day 6 - Probably a Fire Hazard
# http://adventofcode.com/2015/day/6

import sys

# Run one instruction and return the resulting lights array
def run_instruction(instruction, lights):
    action, x_min, y_min, x_max, y_max = parse_instruction(instruction)
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            if action == 'turn on':
                lights[x][y] = True
            elif action == 'turn off':
                lights[x][y] = False
            elif action == 'toggle':
                lights[x][y] = not lights[x][y]
    return lights

# Parse one instruction
def parse_instruction(instruction):
    if instruction.startswith('turn on'):
        action = 'turn on'
    elif instruction.startswith('turn off'):
        action = 'turn off'
    elif instruction.startswith('toggle'):
        action = 'toggle'
    else:
        action = None
    corners = instruction[len(action):].strip().split(' through ')
    x_min, y_min = map(int, corners[0].split(','))
    x_max, y_max = map(int, corners[1].split(','))
    return action, x_min, y_min, x_max, y_max

# Count the lights that are in a lit state
def count_lit_lights(lights):
    return sum(map(sum, lights))

# Main
lights = [[False for x in range(1000)] for y in range(1000)]
for instruction in sys.stdin:
    lights = run_instruction(instruction, lights)
print(count_lit_lights(lights))
