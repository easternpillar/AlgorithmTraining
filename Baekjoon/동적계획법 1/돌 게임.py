# Problem:
# Reference: https://www.acmicpc.net/problem/9655

# My Solution:
import sys

num = int(sys.stdin.readline().rstrip())
dp = [False for _ in range(num + 1)]
dp[0] = True

for i in range(2, num + 1):
    if i - 2 >= 0:
        if dp[i - 2]:
            dp[i] = True

if dp[num]:
    print('CY')
else:
    print('SK')
