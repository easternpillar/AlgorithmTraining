# Problem:
# Reference: https://www.acmicpc.net/problem/2075

# My Solution:
import sys
import heapq

N = int(sys.stdin.readline().rstrip())
candidates = []
for i in range(N):
    candidates.extend(list(map(int, sys.stdin.readline().split())))
    candidates = heapq.nlargest(N, candidates)

print(min(candidates))
