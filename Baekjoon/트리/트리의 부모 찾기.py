# Problem:
# Reference: https://www.acmicpc.net/problem/11725

# My Solution:
import sys
from collections import deque


def bfs(start):
    global parents
    q = deque([start])
    visited = set()
    while q:
        pop = q.popleft()
        if pop in visited:
            continue
        visited.add(pop)
        for c in graph[pop]:
            if c not in visited:
                q.append(c)
                parents[c] = pop


N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N + 1)]
parents = [0 for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)
for i in range(2, N + 1):
    print(parents[i])
