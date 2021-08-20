# Problem:
# Reference: https://www.acmicpc.net/problem/14938

# My Solution:
import math
import sys
from collections import defaultdict
import heapq


def dijkstra(start):
    hq = [start]
    distances = [math.inf for _ in range(n + 1)]
    distances[start[1]] = 0
    answer = 0
    while hq:
        distance, pos = heapq.heappop(hq)

        if distance > distances[pos]:
            continue

        if distance <= m:
            answer += items[pos]
            for con in conn[pos]:
                if distance + con[1] < distances[con[0]]:
                    distances[con[0]] = distance + con[1]
                    heapq.heappush(hq, (distances[con[0]], con[0]))

    return answer


n, m, r = map(int, sys.stdin.readline().split())
items = [0]
items.extend(list(map(int, sys.stdin.readline().split())))
conn = defaultdict(list)
nodes = set()
for _ in range(r):
    f, t, l = map(int, sys.stdin.readline().split())
    conn[f].append((t, l))
    conn[t].append((f, l))

maxi = max(items)
for start in range(1, n + 1):
    maxi = max(maxi, dijkstra((0, start)))
print(maxi)
