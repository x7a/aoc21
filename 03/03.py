#! /usr/bin/env python3

import sys
from collections import Counter

file = sys.argv[1]

with open(file, 'r') as fp:
    vals = [val for val in fp.read().splitlines()]


def bit_counts(arr):
    counts = []
    for i in range(len(arr[0])):
        counts.append(Counter([elem[i] for elem in arr]))
    return counts


def part1():
    gamma = epsilon = ''
    counts = bit_counts(vals)

    for count in counts:
        gamma += count.most_common(1)[0][0]
        epsilon += min(count, key=count.get)
    gamma, epsilon = int(gamma, 2), int(epsilon, 2)

    return gamma * epsilon


def part2():
    left = vals[:]
    i = 0
    while len(left) > 1:
        counts = bit_counts(left)
        digit = '0' if counts[i]['0'] > counts[i]['1'] else '1'
        left = [val for val in left if val[i] == digit]
        i += 1
    oxygen = int(left[0], 2)

    left = vals[:]
    i = 0
    while len(left) > 1:
        counts = bit_counts(left)
        digit = '1' if counts[i]['0'] > counts[i]['1'] else '0'
        left = [val for val in left if val[i] == digit]
        i += 1
    carbon = int(left[0], 2)

    return oxygen * carbon


print(part1())
print(part2())
