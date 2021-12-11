#! /usr/bin/env python3

import sys

file = sys.argv[1]

with open(file, 'r') as fp:
    raw = fp.read().splitlines()

nums = [int(val) for val in raw[0].split(',')]
boards = []

for line in raw[1:]:
    if not line:
        boards.append([])
        continue
    boards[-1].append([int(char) for char in line.split()])

N = len(boards)


def calc_unmarked_sum(board, marked):
    unmarked_sum = 0
    for y in range(5):
        for x in range(5):
            if not marked[y][x]:
                unmarked_sum += board[y][x]
    return unmarked_sum


marked_boards = [[[False] * 5 for j in range(5)] for i in range(len(boards))]
wins = []

# Cycling through every number.
for num in nums:
    # Mark all occurences of current number.
    for i in range(N):
        for y in range(5):
            for x in range(5):
                if boards[i][y][x] == num:
                    marked_boards[i][y][x] = True

    for i, marked in enumerate(marked_boards):
        if i in wins:  # If this board has already won, skip it.
            continue

        for row in marked:
            if all(row):
                if not wins:
                    first_score = calc_unmarked_sum(boards[i], marked) * num
                wins.append(i)
                break
            if len(wins) == N:
                break
        else:  # If no row match was found, we check columns.
            for col in map(list, zip(*marked)):
                if all(col):
                    if not wins:
                        first_score = calc_unmarked_sum(boards[i], marked) * num
                    wins.append(i)
                    break
                if len(wins) == N:
                    break

        if len(wins) == N:
            break

    if len(wins) == N:
        break

last_score = calc_unmarked_sum(boards[wins[-1]], marked_boards[wins[-1]]) * num

print(first_score)  # Solution of part 1.
print(last_score)  # Solution of part 2.
