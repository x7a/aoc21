#! /usr/bin/env python3

import sys

file = sys.argv[1]

with open(file, 'r') as fp:
    crabs = sorted([int(crab) for crab in fp.read().split(',')])

N = len(crabs)

median = crabs[N // 2]
print(sum([abs(median - crab) for crab in crabs]))  # Solution of part 1.

cost = min(sum(sum(range(1, abs(i - c) + 1)) for c in crabs) for i in range(N))
print(cost)  # Solution of part 2.

