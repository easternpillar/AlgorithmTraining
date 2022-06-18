# Problem:
# Reference: https://www.acmicpc.net/problem/1005

# My Solution:
import sys
from collections import deque


def topology(N, conn, indegree, times,tots):
    q = deque([])
    for i in range(N + 1):
        if indegree[i] == 0:
            q.append((i, times[i - 1]))

    while q:
        num, time = q.popleft()
        for con in conn[num]:
            indegree[con] -= 1
            tots[con-1] = max(tots[con-1], times[con-1] + time)
            if indegree[con] == 0:
                q.append((con, tots[con-1]))


for _ in range(int(sys.stdin.readline().rstrip())):
    N, K = map(int, sys.stdin.readline().split())
    conn = [[] for _ in range(N + 1)]
    indegree = [0 for _ in range(N + 1)]
    indegree[0] = -1
    times = list(map(int, sys.stdin.readline().split()))
    tots = times[:]

    for i in range(K):
        f, t = map(int, sys.stdin.readline().split())
        conn[f].append(t)
        indegree[t] += 1

    topology(N, conn, indegree, times,tots)
    W = int(sys.stdin.readline().rstrip())
    print(tots[W - 1])
