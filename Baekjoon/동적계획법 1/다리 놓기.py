# Problem:
# Reference: https://www.acmicpc.net/problem/1010

# My Solution:
import sys

T = int(sys.stdin.readline().rstrip())
board = [[0 for _ in range(31)] for _ in range(31)]
for i in range(31):
    board[1][i] = i

for i in range(2, 31):
    for j in range(i, 31):
        board[i][j] = board[i - 1][j - 1] + board[i][j - 1]

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(board[N][M])
