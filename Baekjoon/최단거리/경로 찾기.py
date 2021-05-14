# Problem:
# Reference: https://www.acmicpc.net/problem/11403

# My Solution:
import sys
from collections import deque


def bfs(s, e):
    q = deque()
    visited = set()

    if s == e:
        for c in conn[s]:
            q.append(c)
    else:
        q = deque([s])

    while q:
        pop = q.popleft()

        if pop == e:
            return True

        if pop in visited:
            continue

        visited.add(pop)

        for c in conn[pop]:
            if c not in visited:
                q.append(c)

    return False


N = int(sys.stdin.readline().rstrip())
conn = [[] for _ in range(N)]
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(len(temp)):
        if temp[j] == 1:
            conn[i].append(j)

answer = [[0 for _ in range(N)] for _ in range(N)]
for i in range(len(answer)):
    for j in range(len(answer)):
        if bfs(i, j):
            answer[i][j] = 1
        else:
            answer[i][j] = 0

for a in answer:
    print(*a)
