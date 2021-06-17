# Problem:
# Reference: https://www.acmicpc.net/problem/2178

# My Solution:
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int, list(sys.stdin.readline().rstrip()))))

visited = [[False for _ in range(M)] for _ in range(N)]
start = (0, 0)
q = deque([[start, 1]])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while q:
    pos, dis = q.popleft()
    if pos == (N - 1, M - 1):
        print(dis)
        break

    if visited[pos[0]][pos[1]]:
        continue

    visited[pos[0]][pos[1]] = True

    for i in range(4):
        nx = pos[0] + dx[i]
        ny = pos[1] + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 1:
                q.append([(nx, ny), dis + 1])
