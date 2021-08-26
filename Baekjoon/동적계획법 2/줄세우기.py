# Problem:
# Reference: https://www.acmicpc.net/problem/2631

# My Solution:
import sys

order = []
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    order.append(int(sys.stdin.readline().rstrip()))
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i - 1, -1, -1):
        if order[j] <= order[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N-max(dp))
