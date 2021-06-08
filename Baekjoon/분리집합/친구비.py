# Problem:
# Reference: https://www.acmicpc.net/problem/16562

# My Solution:
import sys
from collections import deque


def bfs(start):
    q = deque([start])
    mini = costs[start - 1]

    while q:
        pop = q.popleft()
        visited[pop] = True

        for c in conn[pop]:
            if not visited[c]:
                q.append(c)
                mini = min(mini, costs[c - 1])

    return mini


N, M, k = map(int, sys.stdin.readline().split())
costs = list(map(int, sys.stdin.readline().split()))
conn = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(M):
    v, w = map(int, sys.stdin.readline().split())
    conn[v].append(w)
    conn[w].append(v)

tot = 0
for i in range(1, N + 1, 1):
    if visited[i]:
        continue
    tot += bfs(i)

if tot > k:
    print("Oh no")
else:
    print(tot)
