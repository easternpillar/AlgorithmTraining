# Problem:
# Reference: https://www.acmicpc.net/problem/21318

# My Solution:
import sys

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(N + 1)]

for i in range(1, len(nums)):
    if nums[i] < nums[i - 1]:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = dp[i - 1]

dp[-1] = dp[-2]

for _ in range(int(sys.stdin.readline().rstrip())):
    f, t = map(int, sys.stdin.readline().split())
    print(dp[t - 1] - dp[f - 1])
