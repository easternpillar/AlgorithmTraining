# Problem:
# Given a NxN site of the track, return the minimum cost to get the (n, n).
# Condition(s):
# The cost of a straightway is 100.
# The cost of a corner is 500.
# The track can not be built on the wall.

# My Solution:
from collections import deque


def solution(board):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    N = len(board)
    visited = [[-1] * N for _ in range(N)]
    Q = deque()
    Q.append([0, 0, 0, 0])
    Q.append([0, 0, 0, 1])
    visited[0][0] = 0
    while Q:
        now_cost, i, j, d = Q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if ni < 0 or nj < 0 or ni >= N or nj >= N:
                continue

            if board[ni][nj] == 1:
                continue

            if abs(k - d) == 2:
                continue
            cost = 100 if k == d else 600
            new_cost = now_cost + cost
            if visited[ni][nj] == -1 or new_cost <= visited[ni][nj]:
                visited[ni][nj] = new_cost
                Q.append([new_cost, ni, nj, k])

    return visited[N - 1][N - 1]
