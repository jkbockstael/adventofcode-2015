# Advent of Code 2015 - Day 21 - RPG Simulator 20XX
# http://adventofcode.com/2015/day/21

import sys

def parse_input(lines):
    boss = {}
    for line in lines:
        key, value = line.rstrip().split(': ')
        if key == 'Hit Points':
            boss['hp'] = int(value)
        if key == 'Damage':
            boss['da'] = int(value)
        if key == 'Armor':
            boss['ar'] = int(value)
    return boss

def victory(outcome):
    hero, boss = outcome
    return hero['hp'] > 0 and boss['hp'] <= 0

def combat(hero, boss):
    hero_turn = True
    while hero['hp'] > 0 and boss['hp'] > 0:
        if hero_turn:
            attack = hero['da'] - boss['ar']
            boss['hp'] -= attack if attack > 1 else 1
        else:
            attack = boss['da'] - hero['ar']
            hero['hp'] -= attack if attack > 1 else 1
        hero_turn = not hero_turn
    return (hero, boss)

def make_outfits(weapons, armours, rings):
    outfits = []
    for weapon in weapons:
        for armour in armours:
            for left_ring in rings:
                for right_ring in rings:
                    if left_ring == right_ring and left_ring['co'] != 0:
                        continue
                    outfit = {}
                    for stat in ['co', 'ar', 'da']:
                        outfit[stat] = weapon[stat] + armour[stat] + left_ring[stat] + right_ring[stat]
                    outfits.append(outfit)
    return outfits

def equip(hero, outfit):
    equipped = {'co': 0, 'hp': hero['hp'], 'da': hero['da'], 'ar': hero['ar']}
    for stat in ['co', 'ar', 'da']:
        equipped[stat] += outfit[stat]
    return equipped

def cheapest_victory(weapons, armours, rings, hero, boss):
    outfits = make_outfits(weapons, armours, rings)
    equipped = [equip(hero, outfit) for outfit in outfits]
    good_outfits = [o for o in equipped if victory(combat(o, boss.copy()))]
    by_cost = sorted(good_outfits, key = lambda outfit: outfit['co'])
    return by_cost[0]['co']

weapons = [
    {'co': 8, 'da': 4, 'ar': 0}, 
    {'co': 10, 'da': 5, 'ar': 0},
    {'co': 25, 'da': 6, 'ar': 0},
    {'co': 40, 'da': 7, 'ar': 0},
    {'co': 74, 'da': 8, 'ar': 0}
    ]
armours = [
    {'co': 0, 'ar': 0, 'da': 0}, # no armor
    {'co': 13, 'ar': 1, 'da': 0},
    {'co': 31, 'ar': 2, 'da': 0},
    {'co': 53, 'ar': 3, 'da': 0},
    {'co': 75, 'ar': 4, 'da': 0},
    {'co': 102, 'ar': 5, 'da': 0},
    ]
rings = [
    {'co': 0, 'ar': 0, 'da': 0}, # no ring
    {'co': 25, 'da': 1, 'ar': 0},
    {'co': 50, 'da': 2, 'ar': 0},
    {'co': 100, 'da': 3, 'ar': 0},
    {'co': 20, 'ar': 1, 'da': 0},
    {'co': 40, 'ar': 2, 'da': 0},
    {'co': 80, 'ar': 3, 'da': 0}
    ]
boss = parse_input(sys.stdin.readlines())
hero = {'hp': 100, 'da': 0, 'ar': 0}

# Main
if __name__ == '__main__':
    print(cheapest_victory(weapons, armours, rings, hero, boss))
