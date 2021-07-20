# Problem:
# Reference: https://www.acmicpc.net/problem/1753

# My Solution:
import sys
import heapq
import math

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline().rstrip())
conn = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    conn[u].append((w, v))

hq = []
costs = [math.inf for _ in range(V + 1)]
heapq.heappush(hq, (0, K))
costs[K] = 0

while hq:
    cost, node = heapq.heappop(hq)
    if cost > costs[node]:
        continue

    for con in conn[node]:
        if con[0] + cost < costs[con[1]]:
            costs[con[1]] = cost + con[0]
            heapq.heappush(hq, (con[0] + cost, con[1]))

for i in range(1, V + 1):
    if costs[i] == math.inf:
        print("INF")
    else:
        print(costs[i])
