# Problem:
# Reference: https://www.acmicpc.net/problem/7576

# My Solution:
import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
box = []
q = deque([])
riped = 0
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if temp[j] == 1:
            q.append(((i, j), 0))
        elif temp[j] == -1:
            riped += 1
    box.append(temp)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
t_day = 0

while q:
    pos, day = q.popleft()
    if box[pos[0]][pos[1]]==-1:
        continue
    t_day = max(t_day, day)
    riped += 1
    box[pos[0]][pos[1]] = -1
    for i in range(4):
        nx = pos[0] + dx[i]
        ny = pos[1] + dy[i]
        if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
            q.append(((nx, ny), day + 1))

if riped == M * N:
    print(t_day)
else:
    print(-1)
