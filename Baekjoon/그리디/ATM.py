# Problem:
# Reference: https://www.acmicpc.net/problem/11399

# My Solution:
import sys

N = int(sys.stdin.readline().rstrip())
times = list(map(int, sys.stdin.readline().split()))
times.sort()
add = 0
tot = 0
for time in times:
    tot += time + add
    add += time
print(tot)
