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

# Learned:
# 1. sys.stdin.readline().rstrip().split(): faster method for getting inputs.