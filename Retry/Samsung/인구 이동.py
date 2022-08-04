# Reference: https://www.acmicpc.net/problem/16234
import sys
from collections import deque


N, L, R = map(int, sys.stdin.readline().split())
populations = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
days = 0
while True:
    flag = False
    visited = [[False for _ in range(N)] for _ in range(N)]
    groups = []
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            group = {(i, j)}
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                if visited[x][y]:
                    continue
                visited[x][y] = True
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and L <= abs(
                            populations[x][y] - populations[nx][ny]) <= R:
                        q.append((nx, ny))
                        group.add((nx, ny))
                        flag = True
            groups.append(group)
    for group in groups:
        tot = 0
        cnt = len(group)
        for g in group:
            tot += populations[g[0]][g[1]]
        cons = tot // cnt
        for g in group:
            populations[g[0]][g[1]] = cons
    if not flag:
        break
    days += 1
print(days)
