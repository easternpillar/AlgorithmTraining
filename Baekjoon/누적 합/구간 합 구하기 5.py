# Problem:
# Reference: https://www.acmicpc.net/problem/11660

# My Solution:
import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i - 1 >= 0 and j - 1 >= 0:
            board[i][j] += board[i - 1][j] + board[i][j - 1] - board[i - 1][j - 1]
        elif i - 1 >= 0:
            board[i][j] += board[i - 1][j]
        elif j - 1 >= 0:
            board[i][j] += board[i][j - 1]


for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    tot = board[x2 - 1][y2 - 1]
    if x1 > 1 and y1 > 1:
        tot -= board[x2 - 1][y1 - 2] + board[x1 - 2][y2 - 1] - board[x1 - 2][y1 - 2]
    elif x1 > 1:
        tot -= board[x1 - 2][y2 - 1]
    elif y1 > 1:
        tot -= board[x2 - 1][y1 - 2]
    print(tot)
