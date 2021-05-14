# Problem:
# Given the size of map, the position of a dice, and the number of commands, return the number of dice's top.
# Condition(s):
# 1. The number of map will be copied if the number is not 0.
# 2. The number of dice will be copied if the number of map is 0.

# My Solution:
from collections import deque

temp = list(map(int, list(input().split())))
row, col, pos, n = temp[0], temp[1], [temp[2], temp[3]], temp[4]

board = [[0 for i in range(col)] for j in range(row)]

for i in range(row):
    temp_pos = list(map(int, list(input().split())))
    for j in range(col):
        board[i][j] = temp_pos[j]

commands = list(map(int, list(input().split())))
q = deque(commands)

lr = [0, 0, 0, 0]
lr = deque(lr)
ud = [0, 0, 0, 0]
ud = deque(ud)

while q:
    p = q.popleft()
    if p == 1:
        if pos[1] + 1 >= col:
            continue

        pos[1] += 1
        lr.appendleft(lr.pop())
        ud[0] = lr[0]
        ud[2] = lr[2]

    elif p == 2:
        if pos[1] - 1 < 0:
            continue

        pos[1] -= 1
        lr.append(lr.popleft())
        ud[0] = lr[0]
        ud[2] = lr[2]

    elif p == 3:
        if pos[0] - 1 < 0:
            continue

        pos[0] -= 1
        ud.append(ud.popleft())
        lr[0] = ud[0]
        lr[2] = ud[2]

    else:
        if pos[0] + 1 >= row:
            continue

        pos[0] += 1
        ud.appendleft(ud.pop())
        lr[0] = ud[0]
        lr[2] = ud[2]

    if board[pos[0]][pos[1]] == 0:
        board[pos[0]][pos[1]] = lr[2]

    else:
        lr[2] = board[pos[0]][pos[1]]
        ud[2] = board[pos[0]][pos[1]]
        board[pos[0]][pos[1]] = 0

    print(lr[0])
