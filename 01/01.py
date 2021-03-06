#! /usr/bin/env python3

import sys

file = sys.argv[1]

with open(file, 'r') as fp:
    vals = [int(val) for val in fp.read().splitlines()]


def part1():
    larger = 0
    for i, val in enumerate(vals):
        if i == 0:
            continue
        if val > vals[i - 1]:
            larger += 1
    return larger


def part2():
    larger = 0
    sums = [val + vals[i + 1] + vals[i + 2] for i, val in enumerate(vals[:-2])]
    for i, su in enumerate(sums):
        if i == 0:
            continue
        if su > sums[i - 1]:
            larger += 1
    return larger


print(part1())
print(part2())
