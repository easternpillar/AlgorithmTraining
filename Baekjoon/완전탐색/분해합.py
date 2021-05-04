# Problem:
# Reference: https://www.acmicpc.net/problem/2231

# My Solution:
import sys


def const(n):
    tot = 0
    while True:
        n, r = divmod(n, 10)
        tot += r
        if n == 0:
            return tot


N = int(sys.stdin.readline().rstrip())
num = 0
while True:
    if num >= N:
        print(0)
        break
    if N == const(num) + num:
        print(num)
        break
    num += 1
