# Problem:
# Reference: https://www.acmicpc.net/problem/7569

# My Solution:
import sys
from collections import deque


def bfs(q):
    dx = [0, 0, 1, -1, 0, 0]
    dy = [1, -1, 0, 0, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    maxi = 0
    riped = 0
    while q:
        pos, days = q.popleft()
        maxi = max(days, maxi)
        for i in range(6):
            nx = pos[0] + dx[i]
            ny = pos[1] + dy[i]
            nz = pos[2] + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                if tomato[nz][nx][ny] == 0:
                    tomato[nz][nx][ny] = 1
                    riped += 1
                    q.append(((nx, ny, nz), days + 1))
    return riped, maxi


M, N, H = map(int, sys.stdin.readline().split())
q = deque([])
tomato = []
tobe = 0
for i in range(H):
    temp1 = []
    for j in range(N):
        temp2 = list(map(int, sys.stdin.readline().split()))
        for k in range(M):
            if temp2[k] == 1:
                q.append(((j, k, i), 0))
            elif temp2[k] == 0:
                tobe += 1
        temp1.append(temp2)
    tomato.append(temp1)
r, m = bfs(q)
if r != tobe:
    print(-1)
else:
    print(m)
