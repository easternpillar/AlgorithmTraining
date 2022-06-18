# Problem:
# Reference: https://www.acmicpc.net/problem/12865

# My Solution:
import sys

N, K = map(int, sys.stdin.readline().split())
stuffs = []
stuffs = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    W, V = stuffs[i - 1]
    for j in range(K + 1):
        if j - W >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i-1][j - W] + V)
        elif j >= 0:
            dp[i][j] = dp[i - 1][j]
print(dp[N][K])
