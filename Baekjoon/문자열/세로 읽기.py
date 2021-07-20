# Problem:
# Reference: https://www.acmicpc.net/problem/10798

# My Solution:
import sys

maxi = -1
board = []
for i in range(5):
    temp = list(sys.stdin.readline().rstrip())
    board.append(temp)
    maxi = max(maxi, len(temp))

for i in range(maxi):
    for j in range(5):
        if len(board[j]) > i:
            print(board[j][i], end="")
