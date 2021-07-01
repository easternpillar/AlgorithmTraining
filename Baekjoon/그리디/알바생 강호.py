# Problem:
# https://www.acmicpc.net/problem/1758

# My Solution:
import sys

N = int(sys.stdin.readline().rstrip())
tips = []
for _ in range(N):
    tips.append(int(sys.stdin.readline().rstrip()))

tips.sort(reverse=True)
tot = 0
for i in range(len(tips)):
    if tips[i] - i >= 0:
        tot += tips[i] - i

print(tot)
