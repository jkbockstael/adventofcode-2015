# Advent of Code 2015 - Day 7 - Some Assembly Required - Part 2
# http://adventofcode.com/2015/day/7

import sys

GATE_INPUT = 0
GATE_NOT = 1
GATE_AND = 2
GATE_OR = 3
GATE_RSHIFT = 4
GATE_LSHIFT = 5
GATE_CONNECT = 6

# Parse the input and return a map
def parse_input(s):
    circuit = {}
    for line in s:
        gate, output = line.strip().split(' -> ')
        if gate.isdigit():
            operator = GATE_INPUT
            operand_a = int(gate)
            operand_b = None
        elif 'NOT' in gate:
            operator = GATE_NOT
            operand_a = gate[4:]
            operand_b = None
        elif 'AND' in gate:
            operator = GATE_AND
            operand_a, operand_b = gate.split(' AND ')
        elif 'OR' in gate:
            operator = GATE_OR
            operand_a, operand_b = gate.split(' OR ')
        elif 'RSHIFT' in gate:
            operator = GATE_RSHIFT
            operand_a, operand_b = gate.split(' RSHIFT ')
            operand_b = int(operand_b)
        elif 'LSHIFT' in gate:
            operator = GATE_LSHIFT
            operand_a, operand_b = gate.split(' LSHIFT ')
            operand_b = int(operand_b)
        else:  # eg a -> b
            operator = GATE_CONNECT
            operand_a = gate
            operand_b = None
        circuit[output] = (operator, operand_a, operand_b)
    return circuit

# Solve the circuit for a given wire
def solve_for(circuit, memo, wire):
    # Some gates have direct inputs
    if wire.isdigit():
        return int(wire)
    if not wire in memo:
        operator, operand_a, operand_b = circuit[wire]
        if operator == GATE_INPUT:
            result = operand_a
        elif operator == GATE_NOT:
            result = ~solve_for(circuit, memo, operand_a)
        elif operator == GATE_AND:
            result = solve_for(circuit, memo, operand_a) & solve_for(circuit, memo, operand_b)
        elif operator == GATE_OR:
            result = solve_for(circuit, memo, operand_a) | solve_for(circuit, memo, operand_b)
        elif operator == GATE_RSHIFT:
            result = solve_for(circuit, memo, operand_a) >> operand_b
        elif operator == GATE_LSHIFT:
            result = solve_for(circuit, memo, operand_a) << operand_b
        elif operator == GATE_CONNECT:
            result = solve_for(circuit, memo, operand_a)
        memo[wire] = result
    return memo[wire]

# Cast as unsigned 16-bit integer
def u16(integer):
    return integer & 0xFFFF

# Main
circuit = parse_input(sys.stdin.readlines())
circuit['b'] = (GATE_INPUT, u16(solve_for(circuit, {}, 'a')), None)  # Solve the circuit for a, use that value as b
print(u16(solve_for(circuit, {}, 'a')))
