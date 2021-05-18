# Problem:
# Reference: https://www.acmicpc.net/problem/1005

# My Solution: DENIED.
# import sys
#
#
# def bfs(w):
#     global D
#
#     if not conn[w]:
#         return D[w]
#     maxi = 0
#     for c in conn[w]:
#         maxi = max(maxi, bfs(c))
#     return D[w] + maxi
#
#
# answer = []
# for _ in range(int(sys.stdin.readline().rstrip())):
#     N, K = map(int, sys.stdin.readline().split())
#     D = list(map(int, sys.stdin.readline().split()))
#     conn = [[] for _ in range(N)]
#
#     for i in range(K):
#         f, t = map(int, sys.stdin.readline().split())
#         conn[t - 1].append(f - 1)
#
#     W = int(sys.stdin.readline().rstrip())
#
#     sys.stdout.write(bfs(W))

import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    building_time = list(map(int, input().split()))
    total_time = [0] * N
    graph = [[] for _ in range(N)]
    indegree = [0] * N
    for _ in range(K):
        start, end = map(int, input().split())
        graph[start - 1].append(end - 1)
        indegree[end - 1] += 1
    winning_build = int(input()) - 1
    q = deque()
    for i in range(N):
        if indegree[i] == 0:
            q.append(i)
    flag = True
    while q and flag:
        curr = q.popleft()
        for nxt in graph[curr]:
            indegree[nxt] -= 1
            total_time[nxt] = max(total_time[nxt], total_time[curr] + building_time[curr])
            if indegree[nxt] == 0:
                q.append(nxt)
                if nxt == winning_build:
                    flag = False
                    break
    total_time[winning_build] += building_time[winning_build]
    print(total_time[winning_build])
