# Reference: https://www.acmicpc.net/problem/14502
import sys
from collections import deque
from itertools import combinations
from copy import deepcopy

N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

candidates = []
q = deque([])
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            q.append((i, j))
        elif board[i][j] == 0:
            candidates.append((i, j))

maxi = 0
for comb in combinations(candidates, 3):
    new_board = deepcopy(board)
    visited = set([])
    new_q = deepcopy(q)
    for c in comb:
        new_board[c[0]][c[1]] = 1

    while new_q:
        x, y = new_q.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited and new_board[nx][ny] == 0:
                new_q.append((nx, ny))
                new_board[nx][ny] = 2

    cnt = 0
    for i in range(N):
        for j in range(M):
            if new_board[i][j] == 0:
                cnt += 1

    maxi = max(maxi, cnt)
print(maxi)
