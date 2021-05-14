# Problem:
# Given the number of cities and information on one-way roads, return the cities with the shortest distance K from the starting city.

# My Solution:
from collections import deque
import sys

N, M, K, X = map(int, sys.stdin.readline().rstrip().split())

connect = [[] for _ in range(N)]
visited = [False for i in range(N)]
visited[X - 1] = True
distance = [0 for _ in range(N)]

for _ in range(M):
    f, t = map(int, sys.stdin.readline().rstrip().split())
    connect[f - 1].append(t)

q = deque([X])
answer = []

while q:
    c = q.popleft()

    for city in connect[c - 1]:
        if not visited[city - 1]:
            q.append(city)
            distance[city - 1] = distance[c - 1] + 1
            visited[city - 1] = True

for i in range(N):
    if distance[i] == K:
        print(i + 1)
if K not in distance:
    print(-1)

# Other Solution:
# import sys
# from collections import deque
#
# N, M, K, X = map(int, sys.stdin.readline().split())
# conn = [[] for _ in range(N + 1)]
# for i in range(M):
#     a, b = map(int, sys.stdin.readline().split())
#     conn[a].append(b)
#
# cnt = 0
# q = deque([[X, 0]])
# answer = []
# visited = set()
# while q:
#     pos, dist = q.popleft()
#
#     if dist > K:
#         break
#
#     if dist == K and pos not in visited:
#         answer.append(pos)
#     visited.add(pos)
#
#     for c in conn[pos]:
#         if c not in visited:
#             q.append([c, dist + 1])
#             visited.add(pos)
#
# if not answer:
#     print(-1)
# else:
#     for a in sorted(answer):
#         print(a)

