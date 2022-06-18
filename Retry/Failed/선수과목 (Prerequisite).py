# Problem:
# Reference: https://www.acmicpc.net/problem/14567

# My Solution:
import sys
from collections import deque


def topology():
    q = deque([])
    answer = [1 for _ in range(N + 1)]

    for i in range(N + 1):
        if indegrees[i] == 0:
            q.append((i, 1))

    while q:
        num, sem = q.popleft()
        answer[num] = sem
        for con in conn[num]:
            indegrees[con] -= 1
            if indegrees[con] == 0:
                q.append((con, sem + 1))
    return answer


N, M = map(int, sys.stdin.readline().split())
indegrees = [0 for _ in range(N + 1)]
indegrees[0] = -1
conn = [[] for _ in range(N + 1)]
for _ in range(M):
    f, t = map(int, sys.stdin.readline().split())
    indegrees[t] += 1
    conn[f].append(t)

print(*topology()[1:])
