# Problem:
# Reference: https://www.acmicpc.net/problem/2075

# My Solution:
import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
q = []
for _ in range(n):
    q.extend(list(map(int, input().split())))
    q = heapq.nlargest(n, q)
print(q[-1])
