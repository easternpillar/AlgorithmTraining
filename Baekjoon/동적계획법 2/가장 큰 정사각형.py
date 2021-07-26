# Problem:
# Reference: https://www.acmicpc.net/problem/1915

# My Solution:
import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]

maxi = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = board[i][j]
            maxi = max(maxi, dp[i][j])
            continue
        if board[i][j] == 1:
            if dp[i - 1][j] > 0 and dp[i][j - 1] > 0 and dp[i - 1][j - 1] > 0:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            else:
                dp[i][j] = board[i][j]
            maxi = max(maxi, dp[i][j])

print(int(maxi ** 2))
