#! /usr/bin/env python3

import sys

file = sys.argv[1]

with open(file, 'r') as fp:
    raw = fp.read().splitlines()

coords = [[tuple(map(int, p.split(','))) for p in s.split(' -> ')] for s in raw]

N = 1000
diagram = [[0] * N for _ in range(N)]
overlaps = 0

for segment in coords:
    x1, y1, x2, y2 = segment[0][0], segment[0][1], segment[1][0], segment[1][1]

    # Only straight segments.
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            diagram[y1][x] += 1
            if diagram[y1][x] == 2:
                overlaps += 1
    elif x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            diagram[y][x1] += 1
            if diagram[y][x1] == 2:
                overlaps += 1

print(overlaps)  # Solution of part 1.

for segment in coords:
    x1, y1, x2, y2 = segment[0][0], segment[0][1], segment[1][0], segment[1][1]

    if x1 == x2 or y1 == y2:  # Only diagonal segments.
        continue

    directions = {
        'x': 1 if x1 < x2 else -1,
        'y': 1 if y1 < y2 else -1
    }

    for i in range(abs(x1 - x2) + 1):
        x, y = x1 + i * directions['x'], y1 + i * directions['y']
        diagram[y][x] += 1
        if diagram[y][x] == 2:
            overlaps += 1

print(overlaps)  # Solution of part 2.
