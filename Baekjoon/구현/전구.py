# Problem:
# Reference: https://www.acmicpc.net/problem/21918

# My Solution:
import sys

N, M = map(int, sys.stdin.readline().split())
bulbs = list(map(int, sys.stdin.readline().split()))
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        bulbs[b - 1] = c
    elif a == 2:
        for i in range(b - 1, c):
            if bulbs[i]:
                bulbs[i] = 0
            else:
                bulbs[i] = 1
    elif a == 3:
        for i in range(b - 1, c):
            bulbs[i] = 0
    elif a == 4:
        for i in range(b - 1, c):
            bulbs[i] = 1
print(*bulbs)
