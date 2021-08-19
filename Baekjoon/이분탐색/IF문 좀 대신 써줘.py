# Problem:
# Reference: https://www.acmicpc.net/problem/19637

# My Solution:
import sys
import bisect

N, M = map(int, sys.stdin.readline().split())
calls = []
powers = []
for _ in range(N):
    a, b = sys.stdin.readline().split()
    calls.append(a)
    powers.append(int(b))
for _ in range(M):
    temp = int(sys.stdin.readline().rstrip())
    idx = bisect.bisect_left(powers, temp)
    print(calls[idx])
