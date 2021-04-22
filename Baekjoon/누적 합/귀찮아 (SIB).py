# Problem:
# Reference: https://www.acmicpc.net/problem/14929

# My Solution:
import sys

n = int(sys.stdin.readline().rstrip())
xs = list(map(int, sys.stdin.readline().split()))

tot = 0
summ = sum(xs)
for i in range(len(xs)):
    summ -= xs[i]
    tot += xs[i] * summ
print(tot)
