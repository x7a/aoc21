#! /usr/bin/env python3

from sys import stdin

vals = [int(val) for val in stdin.readlines()]

ans = 0
for i, val in enumerate(vals):
    if i == 0:
        continue
    if val > vals[i - 1]:
        ans += 1

print(ans)

