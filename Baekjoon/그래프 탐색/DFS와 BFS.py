# Problem:
#

# My Solution:
import sys
from collections import deque


def dfs():
    q = deque([V])
    visited = set()
    answer = []
    while q:
        pop = q.popleft()

        if pop in visited:
            continue

        visited.add(pop)
        answer.append(pop)
        temp = []
        for c in conn[pop]:
            if c not in visited:
                temp.append(c)
        if temp:
            q.extendleft(sorted(temp, reverse=True))

    return answer


def bfs():
    q = deque([V])
    visited = set()
    answer = []
    while q:
        pop = q.popleft()

        if pop in visited:
            continue

        visited.add(pop)
        answer.append(pop)
        temp = []
        for c in conn[pop]:
            if c not in visited:
                temp.append(c)
        if temp:
            q.extend(sorted(temp))
    return answer


N, M, V = map(int, sys.stdin.readline().split())
conn = [[] for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    conn[v1].append(v2)
    conn[v2].append(v1)

for d in dfs():
    print(d, end=" ")
print()
for b in bfs():
    print(b, end=" ")
