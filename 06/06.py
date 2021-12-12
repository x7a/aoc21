#! /usr/bin/env python3

import sys
from collections import Counter, defaultdict

file = sys.argv[1]

with open(file, 'r') as fp:
    raw = [int(t) for t in fp.read().split(',')]

counts = defaultdict(lambda: 0, Counter(raw))
timers = [counts[i] for i in range(9)]

for day in range(256):
    curr = timers.pop(0)
    timers[6] += curr
    timers.append(curr)

    if day == 79:
        print(sum(timers))  # Solution of part 1.

print(sum(timers))  # Solution of part 2.
