#! /usr/bin/env python3

import sys

file = sys.argv[1]

with open(file, 'r') as fp:
    raw = fp.read().splitlines()

cmds = [(val[0], int(val[1])) for val in [cmd.split() for cmd in raw]]


def part1():
    x = y = 0
    for direction, dist in cmds:
        if direction == 'forward':
            x += dist
        elif direction == 'up':
            y -= dist
        elif direction == 'down':
            y += dist
    return x * y


def part2():
    x = y = aim = 0
    for direction, dist in cmds:
        if direction == 'forward':
            x += dist
            y += aim * dist
        elif direction == 'up':
            aim -= dist
        elif direction == 'down':
            aim += dist
    return x * y


print(part1())
print(part2())
