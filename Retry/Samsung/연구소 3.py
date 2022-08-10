# Reference: https://www.acmicpc.net/problem/17142
from collections import deque
import math
import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
labs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
candidates = []
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)
zeros = 0

for i in range(N):
    for j in range(N):
        if labs[i][j] == 2:
            candidates.append((i, j))
        elif labs[i][j] == 0:
            zeros += 1

answer = math.inf
for comb in combinations(candidates, M):
    q = deque([])
    cnt = 0
    for c in comb:
        q.append((0, c[0], c[1]))

    time = 0
    visited = set()
    flag = True
    while q:
        t, x, y = q.popleft()
        if cnt == zeros:
            break
        if (x, y) in visited:
            continue
        if labs[x][y] == 0:
            cnt += 1
        time = t
        visited.add((x, y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if labs[nx][ny] == 0 and (nx, ny) not in visited:
                    q.append((t + 1, nx, ny))
                elif labs[nx][ny] == 2 and (nx, ny) not in visited:
                    q.append((t + 1, nx, ny))
    if zeros == cnt:
        answer = min(answer, time)
if answer == math.inf:
    print(-1)
else:
    print(answer)
