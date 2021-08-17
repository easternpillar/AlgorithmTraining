# Problem:
# Reference: https://www.acmicpc.net/problem/1463

# My Solution:
import math
import sys

N = int(sys.stdin.readline().rstrip())
if N < 1:
    print(math.inf)
else:
    dp = [math.inf for _ in range(10 ** 6 + 1)]
    dp[1] = 0
    for i in range(2, N + 1):
        if i % 6 == 0:
            dp[i] = min(dp[i - 1], dp[i // 2], dp[i // 3]) + 1
        elif i % 2 == 0:
            dp[i] = min(dp[i - 1], dp[i // 2]) + 1
        elif i % 3 == 0:
            dp[i] = min(dp[i - 1], dp[i // 3]) + 1
        else:
            dp[i]=dp[i-1]+1
    print(dp[N])
