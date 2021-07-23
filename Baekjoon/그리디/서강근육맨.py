# Problem:
# Reference: https://www.acmicpc.net/problem/20300

# My Solution:
import sys

N = int(sys.stdin.readline().rstrip())
level = list(map(int, sys.stdin.readline().split()))
level.sort()
if N % 2 == 0:
    maxi = -1
    for i in range(len(level) // 2):
        maxi = max(maxi, level[i] + level[N - i - 1])
    print(maxi)
else:
    pop = level.pop()
    maxi = -1
    for i in range(len(level) // 2):
        maxi = max(maxi, level[i] + level[N - i - 2])
    print(maxi)
