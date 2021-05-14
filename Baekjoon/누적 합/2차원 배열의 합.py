# Problem:
# https://www.acmicpc.net/problem/2167

# My Solution:
import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if i - 1 < 0 and j - 1 < 0:
            continue
        elif i - 1 < 0:
            board[i][j] += board[i][j - 1]
        elif j - 1 < 0:
            board[i][j] += board[i - 1][j]
        else:
            board[i][j] += board[i - 1][j] + board[i][j - 1] - board[i - 1][j - 1]

for i in range(int(sys.stdin.readline().rstrip())):
    r1, c1, r2, c2 = list(map(int, sys.stdin.readline().split()))
    r1 -= 1
    r2 -= 1
    c1 -= 1
    c2 -= 1
    if r1 - 1 < 0 and c1 - 1 < 0:
        print(board[r2][c2])
    elif r1 - 1 < 0:
        print(board[r2][c2] - board[r2][c1 - 1])
    elif c1 - 1 < 0:
        print(board[r2][c2] - board[r1 - 1][c2])
    else:
        print(board[r2][c2] - board[r2][c1 - 1] - board[r1 - 1][c2] + board[r1 - 1][c1 - 1])
