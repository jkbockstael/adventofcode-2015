# Advent of Code 2015 - Day 14 - Reindeer Olympics
# http://adventofcode.com/day/14

import sys

# Parse reindeer descriptions as a list of tuples
def parse_reindeers(reindeer_specs):
    def parse_reindeer(reindeer_spec):
        tokens = reindeer_spec.split(' ')
        speed, fly_time, rest_time = int(tokens[3]), int(tokens[6]), int(tokens[13])
        return (speed, fly_time, rest_time)
    return [parse_reindeer(reindeer_spec) for reindeer_spec in reindeer_specs]

# Calculte the traveled distances for all reindeers after a given time
def distances_traveled(reindeers, time):
    def distance_traveled(reindeer, time):
        speed, fly_time, rest_time = reindeer
        flights = (time // (fly_time + rest_time))
        extra_time = time % (fly_time + rest_time)
        extra_distance = speed * extra_time if (extra_time < fly_time) else fly_time * speed
        return flights * speed * fly_time + extra_distance
    return [distance_traveled(reindeer, time) for reindeer in reindeers]

# Main
if __name__ == '__main__':
    print(max(distances_traveled(parse_reindeers(sys.stdin.readlines()), 2503)))
