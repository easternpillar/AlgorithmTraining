# Problem:
# Given an nxn test tube and k virus locations, return the virus type in x,y coordinates after s seconds.
# Condition(s):
# 1. Viruses spread up, down, left and right in one second.
# 2. Viruses spread in order of virus number.
# 3. There is only one virus in one cell of the test tube.
# 4. If a virus already exists, other viruses can not spread.

# My Solution:
from collections import deque
import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

room = []
virus = [[] for _ in range(K)]

for i in range(N):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(len(temp)):
        if temp[j] != 0:
            virus[temp[j] - 1].append([[i, j], 0])
    room.append(temp)

q = deque()
for i in range(len(virus)):
    q.extend(virus[i])

S, X, Y = map(int, sys.stdin.readline().rstrip().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while q:
    pos, sec = q.popleft()

    if sec >= S:
        break

    for i in range(len(dx)):
        nx = pos[0] + dx[i]
        ny = pos[1] + dy[i]
        if N > nx >= 0 and N > ny >= 0 and room[nx][ny] == 0:
            room[nx][ny] = room[pos[0]][pos[1]]
            q.append([[nx, ny], sec + 1])

print(room[X - 1][Y - 1])
