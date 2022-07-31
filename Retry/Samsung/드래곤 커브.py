# Reference: https://www.acmicpc.net/problem/15685
import sys

N = int(sys.stdin.readline().rstrip())
direction = {0: (0, 1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}
board = [[1 for _ in range(101)] for _ in range(101)]
for _ in range(N):
    x, y, d, g = map(int, sys.stdin.readline().split())
    progress = [d]
    for _ in range(g):
        temp = list(reversed(progress[:]))
        for i in range(len(temp)):
            progress.append((temp[i] + 1) % 4)
    board[y][x] = 0
    for p in progress:
        x += direction[p][1]
        y += direction[p][0]
        board[y][x] = 0
cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 0 and board[i][j + 1] == 0 and board[i + 1][j] == 0 and board[i + 1][j + 1] == 0:
            cnt += 1
print(cnt)
