# Problem:
# Reference: https://www.acmicpc.net/problem/20056

# My Solution:
import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
board = [[deque([]) for _ in range(N)] for _ in range(N)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    board[r - 1][c - 1].append((m, s, d))

for _ in range(K):
    temp_board = [[deque([]) for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            while board[i][j]:
                m, s, d = board[i][j].popleft()
                nx = (i + s * dx[d]) % N
                ny = (j + s * dy[d]) % N
                temp_board[nx][ny].append((m, s, d))

    board = temp_board[:]
    temp_board = [[deque([]) for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if len(board[i][j]) >= 2:
                tm = 0
                ts = 0
                td = 0
                even = []
                while board[i][j]:
                    m, s, d = board[i][j].popleft()
                    tm += m
                    ts += s
                    if d % 2 == 0:
                        even.append(1)
                    else:
                        even.append(0)

                td = sum(even)
                length = len(even)
                if tm // 5 == 0:
                    continue
                else:
                    nm = tm // 5
                    ns = ts // length

                    if td == 0 or td == len(even):
                        for nd in range(0, 8, 2):
                            temp_board[i][j].append((nm, ns, nd))
                    else:
                        for nd in range(1, 9, 2):
                            temp_board[i][j].append((nm, ns, nd))
            else:
                while board[i][j]:
                    pop = board[i][j].popleft()
                    temp_board[i][j].append(pop[:])
    board = temp_board[:]

answer = 0
for i in range(N):
    for j in range(N):
        if board[i][j]:
            for fireball in board[i][j]:
                answer += fireball[0]

print(answer)
