# Problem:
# Reference: https://www.acmicpc.net/problem/9251

# My Solution:
import sys

str1 = list(sys.stdin.readline().rstrip())
str2 = list(sys.stdin.readline().rstrip())
l1 = len(str1)
l2 = len(str2)

board = [[0 for _ in range(l1 + 1)] for _ in range(l2 + 1)]

for i in range(1, l2 + 1):
    for j in range(1, l1 + 1):
        if str2[i - 1] == str1[j - 1]:
            board[i][j] = board[i - 1][j - 1] + 1
        else:
            board[i][j] = max(board[i - 1][j], board[i][j - 1])

print(board[l2][l1])
