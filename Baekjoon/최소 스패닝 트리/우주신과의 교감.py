# Problem:
# Reference: https://www.acmicpc.net/problem/1774

# My Solution:
import sys
import math
import heapq


def calDist():
    for i in range(N):
        for j in range(i + 1, N):
            heapq.heappush(hq, (math.sqrt((gods[i][0] - gods[j][0]) ** 2 + (gods[i][1] - gods[j][1]) ** 2), (i+1, j+1)))


def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    ta = find(a)
    tb = find(b)
    if ta > tb:
        parent[ta] = tb
    else:
        parent[tb] = ta


N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N + 1)]
gods = []
for _ in range(N):
    gods.append(list(map(int, sys.stdin.readline().split())))

hq = []
calDist()

for _ in range(M):
    god1, god2 = map(int, sys.stdin.readline().split())
    union(god1, god2)

answer = 0
while hq:
    dist, god = heapq.heappop(hq)
    if find(god[0]) != find(god[1]):
        union(god[0], god[1])
        answer += dist

print("%.2f" % answer)
