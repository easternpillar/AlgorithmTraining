# Reference: https://www.acmicpc.net/problem/14500
import sys
from collections import deque


def rotate90(board):
    board = list(map(list, zip(*reversed(board))))
    for b in board:
        b = reversed(b)
    return board


def upsideDown(board):
    for b in board:
        b.reverse()
    return board


N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
q = deque([])
maxi = 0

for i in range(0, len(board) - 1, 1):
    for j in range(0, len(board[0]) - 1, 1):
        tot = 0
        tot += board[i][j]
        tot += board[i][j + 1]
        tot += board[i + 1][j]
        tot += board[i + 1][j + 1]
        maxi = max(maxi, tot)

for _ in range(4):
    board = rotate90(board)
    for i in range(0, len(board), 1):
        for j in range(0, len(board[0]) - 3, 1):
            tot = 0
            tot += board[i][j]
            tot += board[i][j + 1]
            tot += board[i][j + 2]
            tot += board[i][j + 3]
            maxi = max(maxi, tot)

    for i in range(0, len(board) - 1, 1):
        for j in range(0, len(board[0]) - 2, 1):
            tot = 0
            tot += board[i][j]
            tot += board[i][j + 1]
            tot += board[i][j + 2]
            tot += board[i + 1][j + 1]
            maxi = max(maxi, tot)

for _ in range(2):
    board = upsideDown(board)
    for _ in range(4):
        board = rotate90(board)
        for i in range(0, len(board) - 2, 1):
            for j in range(0, len(board[0]) - 1, 1):
                tot = 0
                tot += board[i][j]
                tot += board[i + 1][j]
                tot += board[i + 2][j]
                tot += board[i + 2][j + 1]
                maxi = max(maxi, tot)

        for i in range(0, len(board) - 2, 1):
            for j in range(0, len(board[0]) - 1, 1):
                tot = 0
                tot += board[i][j]
                tot += board[i + 1][j]
                tot += board[i + 1][j + 1]
                tot += board[i + 2][j + 1]
                maxi = max(maxi, tot)
print(maxi)
