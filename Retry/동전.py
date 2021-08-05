# Problem:
# Reference: https://www.acmicpc.net/problem/9084

# My Solution:
import sys

answer=[]
for _ in range(int(sys.stdin.readline().rstrip())):
    N = int(sys.stdin.readline().rstrip())
    coins = tuple(map(int, sys.stdin.readline().split()))
    target=int(sys.stdin.readline().rstrip())
    dp = [0 for _ in range(target + 1)]
    dp[0] = 1
    for c in coins:
        for i in range(1, target + 1):
            if i - c >= 0:
                dp[i] += dp[i - c]
    answer.append(dp[target])
for a in answer:
    print(a)
