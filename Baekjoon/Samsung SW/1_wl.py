# Problem:
# Given a mxn table, a red ball, and a blue ball, return the minimum number that makes the red ball in the hole.
# Condition(s):
# 1. Only one side can be tilted at a time.
# 2. Return -1 if the number of tilting exceeds 10.

# My Solution:
import sys

row, col = map(int, input().split())

li = []
for i in range(row):
    li.append(list(input()))

red = blue = hole = None
for i in range(row):
    for j in range(col):
        if li[i][j] == 'R':
            red = [i, j]
            continue
        if li[i][j] == 'B':
            blue = [i, j]
            continue
        if li[i][j] == 'O':
            hole = [i, j]

stack = [[red, 0, blue]]
used = []
cnt = 0
answer = -1

while stack:
    temp = stack.pop(0)
    if temp[1]>=10:
        continue
    red_pos = temp[0].copy()
    blue_pos = temp[2].copy()
    used.append([temp[0], temp[2]])
    cnt = temp[1]
    flag = 1

    while li[blue_pos[0] + 1][blue_pos[1]] != '#':
        blue_pos[0] += 1
        if blue_pos == hole:
            flag = 0
            break

    while li[red_pos[0] + 1][red_pos[1]] != '#':
        red_pos[0] += 1
        if flag == 1 and red_pos == hole:
            print(cnt + 1)
            sys.exit()

    if red_pos == blue_pos:
        if abs(temp[0][0] - red_pos[0]) > abs(temp[2][0] - red_pos[0]):
            red_pos[0] -= 1
        else:
            blue_pos[0] -= 1

    if flag == 1 and [red_pos, blue_pos] not in used:
        stack.append([red_pos, cnt + 1, blue_pos])

    flag = 1
    red_pos = temp[0].copy()
    blue_pos = temp[2].copy()

    while li[blue_pos[0] - 1][blue_pos[1]] != '#':
        blue_pos[0] -= 1
        if blue_pos == hole:
            flag = 0
            break

    while li[red_pos[0] - 1][red_pos[1]] != '#':
        red_pos[0] -= 1
        if flag == 1 and red_pos == hole:
            print(cnt + 1)
            sys.exit()

    if red_pos == blue_pos:
        if abs(temp[0][0] - red_pos[0]) > abs(temp[2][0] - red_pos[0]):
            red_pos[0] += 1
        else:
            blue_pos[0] += 1

    if flag == 1 and [red_pos, blue_pos] not in used:
        stack.append([red_pos, cnt + 1, blue_pos])

    flag = 1
    red_pos = temp[0].copy()
    blue_pos = temp[2].copy()

    while li[blue_pos[0]][blue_pos[1] + 1] != '#':
        blue_pos[1] += 1
        if blue_pos == hole:
            flag = 0
            break

    while li[red_pos[0]][red_pos[1] + 1] != '#':
        red_pos[1] += 1
        if flag == 1 and red_pos == hole:
            print(cnt + 1)
            sys.exit()

    if red_pos == blue_pos:
        if abs(temp[0][1] - red_pos[1]) > abs(temp[2][1] - red_pos[1]):
            red_pos[1] -= 1
        else:
            blue_pos[1] -= 1

    if flag == 1 and [red_pos, blue_pos] not in used:
        stack.append([red_pos, cnt + 1, blue_pos])

    flag = 1
    red_pos = temp[0].copy()
    blue_pos = temp[2].copy()

    while li[blue_pos[0]][blue_pos[1] - 1] != '#':
        blue_pos[1] -= 1
        if blue_pos == hole:
            flag = 0
            break

    while li[red_pos[0]][red_pos[1] - 1] != '#':
        red_pos[1] -= 1
        if flag == 1 and red_pos == hole:
            print(cnt + 1)
            sys.exit()

    if red_pos == blue_pos:
        if abs(temp[0][1] - red_pos[1]) > abs(temp[2][1] - red_pos[1]):
            red_pos[1] += 1

        else:
            blue_pos[1] += 1

    if flag == 1 and [red_pos, blue_pos] not in used:
        stack.append([red_pos, cnt + 1, blue_pos])

print(-1)

# Learned:
# 1. sys module: sys.exit() is used for termination.