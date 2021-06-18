# Problem:
# Reference: https://www.acmicpc.net/problem/21610

# My Solution:
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
A = []

for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

q = deque([(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)])

copy_dx = [-1, -1, 1, 1]
copy_dy = [-1, 1, -1, 1]
for _ in range(M):
    d, s = map(int, sys.stdin.readline().split())
    water_copy = []

    visited = [[False] * N for _ in range(N)]
    while q:
        c = q.popleft()
        nx = (c[0] + dx[d - 1] * s) % N
        ny = (c[1] + dy[d - 1] * s) % N
        A[nx][ny] += 1
        water_copy.append((nx, ny))
        visited[nx][ny] = True

    for wc in water_copy:
        nx, ny = wc[0], wc[1]
        for i in range(4):
            nnx = nx + copy_dx[i]
            nny = ny + copy_dy[i]
            if 0 <= nnx < N and 0 <= nny < N:
                if A[nnx][nny]:
                    A[nx][ny] += 1

    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            if A[i][j] >= 2:
                q.append((i, j))
                A[i][j] -= 2

tot = 0
for a in A:
    tot += sum(a)

print(tot)
