#! /usr/bin/env python3

import sys

file = sys.argv[1]

with open(file, 'r') as fp:
    raw = fp.read().splitlines()
entries = [tuple(part.split() for part in line.split(' | ')) for line in raw]

# Solution of part 1.
unique = [2, 4, 3, 7]
print(sum([1 for ent in entries for dig in ent[1] if len(dig) in unique]))


def get_by_segments(patterns, count):
    return [sorted(pat) for pat in patterns if len(pat) == count]


ans = 0
for entry in entries:
    patterns, outputs = entry
    digits = {}

    digits[1] = get_by_segments(patterns, 2)[0]
    digits[4] = get_by_segments(patterns, 4)[0]
    digits[7] = get_by_segments(patterns, 3)[0]
    digits[8] = get_by_segments(patterns, 7)[0]

    for pattern in get_by_segments(patterns, 6):
        if len(set(pattern) ^ set(digits[4])) == 2:
            digits[9] = pattern
        elif len(set(pattern) ^ set(digits[7])) == 5:
            digits[6] = pattern
        else:
            digits[0] = pattern

    for pattern in get_by_segments(patterns, 5):
        if len(set(pattern) ^ set(digits[1])) == 3:
            digits[3] = pattern
        elif len(set(pattern) ^ set(digits[9])) == 1:
            digits[5] = pattern
        else:
            digits[2] = pattern

    digits = {frozenset(v): k for k, v in digits.items()}

    ans += int(''.join([str(digits[frozenset(output)]) for output in outputs]))

print(ans)  # Solution of part 2.

