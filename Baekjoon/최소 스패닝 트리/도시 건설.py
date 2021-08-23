# Problem:
# Reference: https://www.acmicpc.net/problem/21924

# My Solution:
import sys
import heapq


def find(target):
    if target == parent[target]:
        return parent[target]
    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    ta, tb = find(a), find(b)
    if ta != tb:
        parent[ta] = tb


N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N + 1)]
hq = []
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    heapq.heappush(hq, (c, a, b))

tot = 0
answer = 0
while hq:
    cost, f, t = heapq.heappop(hq)
    tot += cost
    if find(f) != find(t):
        union(f, t)
        answer += cost

p = find(1)
flag = True
for i in range(2, N + 1):
    if p != find(i):
        flag = False
        break
if flag:
    print(tot - answer)
else:
    print(-1)
