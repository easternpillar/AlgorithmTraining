# Reference: https://www.acmicpc.net/problem/14501
import sys

N = int(sys.stdin.readline().rstrip())
days = []
costs = []
dp = [0 for _ in range(N+1)]
for i in range(N):
    d, c = map(int, sys.stdin.readline().split())
    days.append(d)
    costs.append(c)

for i in range(N - 1, -1, -1):
    if days[i] + i > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + days[i]] + costs[i], dp[i + 1])
print(dp[0])
