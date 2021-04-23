# Problem:
# Given the information of prerequisites, print the minimum semesters of each subject to be taken.

# My Solution:
import sys
from collections import deque


def topology():
    res = [0 for _ in range(N + 1)]
    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append((i, 1))
            res[i] = 1

    while q:
        sub, sem = q.popleft()
        res[sub] = sem
        for i in pres[sub]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append((i, sem + 1))

    for i in range(1, len(res)):
        print(res[i], end=' ')


N, M = map(int, sys.stdin.readline().split())
pres = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    pres[A].append(B)
    indegree[B] += 1

topology()
