# Problem:
# Reference: https://www.acmicpc.net/problem/2623

# My Solution:
import sys
from collections import deque


def topology():
    q = deque([])
    answer = []
    for i in range(N + 1):
        if indegrees[i] == 0:
            q.append(i)
    while q:
        node = q.popleft()
        answer.append(node)
        for con in conn[node]:
            indegrees[con] -= 1
            if indegrees[con] == 0:
                q.append(con)
    return answer


N, M = map(int, sys.stdin.readline().split())
indegrees = [0 for _ in range(N + 1)]
indegrees[0] = -1
conn = [[] for _ in range(N + 1)]

for _ in range(M):
    temp = list(map(int, sys.stdin.readline().split()))

    for i in range(2, len(temp), 1):
        indegrees[temp[i]] += 1

        conn[temp[i - 1]].append(temp[i])

answer = topology()
if len(answer) == N:
    for a in answer:
        print(a)
else:
    print(0)
