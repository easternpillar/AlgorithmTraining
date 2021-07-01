# Problem:
# Reference: https://www.acmicpc.net/problem/2225

# My Solution:
import sys

N, K = map(int, sys.stdin.readline().split())
dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]

for i in range(N + 1):
    dp[1][i] = 1

for i in range(1, K + 1):
    dp[i][0] = 1

for i in range(1, K + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[K][N] % 1000000000)
