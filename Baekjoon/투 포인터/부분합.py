# Problem:
# Reference: https://www.acmicpc.net/problem/1806

# My Solution:
import math
import sys

N, S = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))
left = right = 0
length = math.inf
tot = seq[0]
while left <= right < N:
    if tot < S:
        right += 1
        if right < N:
            tot += seq[right]
        else:
            break
    elif tot >= S:
        length = min(length, right - left)
        tot -= seq[left]
        left += 1
        if left > right:
            right = left


if length != math.inf:
    print(length + 1)
else:
    print(0)
