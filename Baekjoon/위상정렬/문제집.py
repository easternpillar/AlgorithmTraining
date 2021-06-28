# Problem:
# Reference: https://www.acmicpc.net/problem/1766

# My Solution:
import sys
import heapq
from collections import defaultdict


def topology():
    hq = []
    answer = []
    for i in range(1, N + 1):
        if indegrees[i] == 0:
            heapq.heappush(hq, i)

    while hq:
        pop = heapq.heappop(hq)
        visited[pop] = True
        for idx in pre[pop]:
            indegrees[idx] -= 1
            if indegrees[idx] == 0:
                heapq.heappush(hq, idx)
        answer.append(pop)
    return answer


N, M = map(int, sys.stdin.readline().split())
indegrees = [0 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
visited[0] = True
pre = defaultdict(list)

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    pre[a].append(b)
    indegrees[b] += 1

print(*topology())
