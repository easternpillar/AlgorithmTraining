# Problem:
# Assuming that 1 is wall, 0 is empty space, and 2 is virus, return the maximum size of safe area.
# Condition(s):
# 1. Virus can be spread if it is connected to empty spaces.
# 2. Only 3 more wall can be built.

# My Solution:
import copy
from collections import deque


def spread(rcpy, pos):
    for a, b in pos:
        rcpy[a][b] = 1

    virus = []
    for i in range(len(rcpy)):
        for j in range(len(rcpy[i])):
            if rcpy[i][j] == 2:
                virus.append([i, j])

    while virus:
        v = virus.pop()
        if v[0] - 1 >= 0:
            if rcpy[v[0] - 1][v[1]] == 0:
                rcpy[v[0] - 1][v[1]] = 2
                virus.append([v[0] - 1, v[1]])
        if v[0] + 1 < len(rcpy):
            if rcpy[v[0] + 1][v[1]] == 0:
                rcpy[v[0] + 1][v[1]] = 2
                virus.append([v[0] + 1, v[1]])
        if v[1] - 1 >= 0:
            if rcpy[v[0]][v[1] - 1] == 0:
                rcpy[v[0]][v[1] - 1] = 2
                virus.append([v[0], v[1] - 1])
        if v[1] + 1 < len(rcpy[0]):
            if rcpy[v[0]][v[1] + 1] == 0:
                rcpy[v[0]][v[1] + 1] = 2
                virus.append([v[0], v[1] + 1])

    cnt = 0
    for i in range(len(rcpy)):
        for j in range(len(rcpy[i])):
            if rcpy[i][j] == 0:
                cnt += 1

    return cnt


r, c = map(int, input().split())

room = []
for i in range(r):
    room.append(list(map(int, list(input().split()))))

q = deque()
for i in range(r):
    for j in range(c):
        if room[i][j] == 0:
            q.append([[i, j]])

answer = set()
while q:
    p = q.popleft()
    if len(p) == 3:
        answer.add(spread(copy.deepcopy(room), p))
        continue
    elif len(p) > 3:
        break
    else:
        for i in range(p[-1][0], r, 1):
            for j in range(c):
                if i == p[-1][0] and j <= p[-1][1]:
                    continue
                if room[i][j] == 0:
                    temp = copy.deepcopy(p)
                    temp.append([i, j])
                    q.append(temp)

print(max(answer))
