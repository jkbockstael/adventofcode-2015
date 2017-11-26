# Advent of Code 2015 - Day 21 - RPG Simulator 20XX - Part 2
# http://adventofcode.com/2015/day/21

from day21_part1 import *

def most_expensive_defeat(weapons, armours, rings, hero, boss):
    outfits = make_outfits(weapons, armours, rings)
    equipped = [equip(hero, outfit) for outfit in outfits]
    bad_outfits = [o for o in equipped if not victory(combat(o, boss.copy()))]
    by_cost = sorted(bad_outfits, key = lambda outfit: outfit['co'])
    return by_cost[-1]['co']

# Main
print(most_expensive_defeat(weapons, armours, rings, hero, boss))
