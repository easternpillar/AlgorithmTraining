# Problem:
# Reference: https://www.acmicpc.net/problem/9095

# My Solution:
import sys

dp = [0 for _ in range(11)]
dp[0] = 1
for i in range(1, 4, 1):
    for j in range(1,11):
        tot = 0
        for k in range(j - i, j, 1):
            if k >= 0:
                tot += dp[k]
        dp[j] = tot
for _ in range(int(sys.stdin.readline().rstrip())):
    num = int(sys.stdin.readline().rstrip())
    print(dp[num])
