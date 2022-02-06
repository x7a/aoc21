#! /usr/bin/env python3

import sys
from functools import reduce

sys.setrecursionlimit(1000000000)

file = sys.argv[1]

with open(file, 'r') as fp:
    heightmap = [[int(pnt) for pnt in line] for line in fp.read().splitlines()]

WIDTH, HEIGHT = len(heightmap[0]), len(heightmap)
ADJACENCY = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def get_adjacents(x, y):
    for dx, dy in ADJACENCY:
        adj_x, adj_y = x + dx, y + dy
        if 0 <= adj_x < WIDTH and 0 <= adj_y < HEIGHT:
            yield adj_x, adj_y


def traversable(x, y, visited):
    return basins[y][x] == 1 and not visited[y][x]


def dfs(x, y, visited):
    size = 0
    visited[y][x] = True
    for adj_x, adj_y in get_adjacents(x, y):
        if traversable(adj_x, adj_y, visited):
            size += dfs(adj_x, adj_y, visited) + 1
    return size


risk_sum = 0
basins = [[0] * WIDTH for _ in range(HEIGHT)]

for y in range(HEIGHT):
    for x in range(WIDTH):
        curr_point = heightmap[y][x]
        low = True

        for adj_x, adj_y in get_adjacents(x, y):
            curr_adj = heightmap[adj_y][adj_x]

            if curr_point < curr_adj:
                continue

            if curr_point != 9 and curr_adj != 9:
                basins[y][x] = 1
            low = False
            break

        if not low:
            continue
        if curr_point != 9:
            basins[y][x] = 1
        risk_sum += curr_point + 1

print(risk_sum)

visited = [[False] * WIDTH for _ in range(HEIGHT)]
sizes = []

for y in range(HEIGHT):
    for x in range(WIDTH):
        if traversable(x, y, visited):
            sizes.append(dfs(x, y, visited) + 1)

size_product = reduce(lambda a, b: a * b, sorted(sizes, reverse=True)[:3])
print(size_product)

