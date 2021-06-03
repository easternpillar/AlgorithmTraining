# Problem:
# Reference: https://www.acmicpc.net/problem/19532

# My Solution:
import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())
for x in range(-999, 1000, 1):
    for y in range(-999, 1000, 1):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            break
