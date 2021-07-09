# Problem:
# Reference: https://www.acmicpc.net/problem/2667

# My Solution:
import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(start):
    q = deque([start])
    cnt = 0
    while q:
        x, y = q.popleft()
        if not visited[x][y]:
            cnt += 1
            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny]==1:
                    q.append((nx, ny))

    return cnt


N = int(sys.stdin.readline().rstrip())
board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

answer = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and board[i][j] == 1:
            answer.append(bfs((i, j)))

print(len(answer))
for a in sorted(answer):
    print(a)
