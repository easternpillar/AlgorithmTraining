# Reference: https://www.acmicpc.net/problem/3190
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())
time = 0

board = [['#' for _ in range(N+2)] for _ in range(N+2)]
for i in range(1, N+1):
    for j in range(1, N+1):
        board[i][j] = 0

for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    board[r][c] = 1

# for b in board:
#     print(b)

direction = [0, 1]
bodies = deque([[1, 1]])
pos = [1, 1]
changes = {}
for _ in range(int(sys.stdin.readline().rstrip())):
    t, d = sys.stdin.readline().split()
    changes[int(t)] = d

# print(changes)


def change(direction, to):
    if direction == [0, 1]:
        if to == 'D':
            return [1, 0]
        else:
            return [-1, 0]

    elif direction == [1, 0]:
        if to == 'D':
            return [0, -1]
        else:
            return [0, 1]

    elif direction == [0, -1]:
        if to == 'D':
            return [-1, 0]
        else:
            return [1, 0]

    elif direction == [-1, 0]:
        if to == 'D':
            return [0, 1]
        else:
            return [0, -1]


while True:
    time += 1
    pos[0] += direction[0]
    pos[1] += direction[1]
    if board[pos[0]][pos[1]] == '#' or [pos[0], pos[1]] in bodies:
        print(time)
        break
    elif board[pos[0]][pos[1]] == 0:
        bodies.pop()
        bodies.appendleft([pos[0], pos[1]])
    else:
        bodies.appendleft([pos[0], pos[1]])
        board[pos[0]][pos[1]] = 0

    if time in changes.keys():
        direction = change(direction, changes[time])
