# Reference: https://www.acmicpc.net/problem/16236
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
pool = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
q = deque([])
flag = False
pos = []
size = 2
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited = set()
answer = 0
for i in range(N):
    for j in range(N):
        if pool[i][j] == 9:
            pos = [i, j]
            q.append((i, j, 0, 0))
            pool[i][j] = 0
            flag = True
            break
    if flag:
        break

while q:
    x, y, distance, eat = q.popleft()
    if (x, y) in visited:
        continue
    visited.add((x, y))
    if pool[x][y] != 0 and pool[x][y] < size:
        answer += distance
        pool[x][y] = 0
        visited = set()
        # print(x, y, " 냠냠")
        # print("이동거리:", distance)
        if eat + 1 == size:
            size += 1
            eat = -1
            # print("성장", size)
        q = deque([(x, y, 0, eat + 1)])
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and pool[nx][ny] <= size and (nx, ny) not in visited:
            q.append((nx, ny, distance + 1, eat))
    q = deque(sorted(list(q), key=lambda x: (x[2], x[0], x[1])))

print(answer)
