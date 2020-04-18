# Problem:
# Given a mxn board with integers for each cell, return the maximum number that can be gotten.
# Condition(s):
# 1. Only 4 attached cells can be gotten.

# My Solution:
import copy


def line(b, pos):
    rl, cl = len(b), len(b[0])
    x, y = pos[0], pos[1]
    if y + 3 >= cl:
        return 0
    else:
        return b[x][y] + b[x][y + 1] + b[x][y + 2] + b[x][y + 3]


def square(b, pos):
    rl, cl = len(b), len(b[0])
    x, y = pos[0], pos[1]
    if x + 1 >= rl or y + 1 >= cl:
        return 0
    else:
        return b[x][y] + b[x + 1][y] + b[x + 1][y + 1] + b[x][y + 1]


def gun(b, pos):
    rl, cl = len(b), len(b[0])
    x, y = pos[0], pos[1]
    if x + 1 >= rl or y + 2 >= cl:
        return 0
    else:
        return b[x][y] + b[x][y + 1] + b[x][y + 2] + b[x + 1][y + 2]


def worm(b, pos):
    rl, cl = len(b), len(b[0])
    x, y = pos[0], pos[1]
    if x + 1 >= rl or y + 2 >= cl:
        return 0
    else:
        return b[x][y] + b[x][y + 1] + b[x + 1][y + 1] + b[x + 1][y + 2]


def mnt(b, pos):
    rl, cl = len(b), len(b[0])
    x, y = pos[0], pos[1]
    if x + 1 >= rl or y + 2 >= cl:
        return 0
    else:
        return b[x][y] + b[x][y + 1] + b[x][y + 2] + b[x + 1][y + 1]


def rot(b):
    b = list(zip(*b))
    for i in range(len(b)):
        b[i] = list(b[i])
        b[i].reverse()
    return b


def leftright(b):
    for i in range(len(b)):
        b[i].reverse()
    return b


row, col = map(int, list(input().split()))
board = []
for i in range(row):
    board.append(list(map(int, list(input().split()))))

answer = set()
temp = copy.deepcopy(board)
for lr in range(2):
    for r in range(4):
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                answer.add(line(temp, [i, j]))
                answer.add(square(temp,[i,j]))
                answer.add(gun(temp, [i, j]))
                answer.add(worm(temp, [i, j]))
                answer.add(mnt(temp, [i, j]))
        temp = rot(temp)
    temp = leftright(temp)

print(max(answer))
