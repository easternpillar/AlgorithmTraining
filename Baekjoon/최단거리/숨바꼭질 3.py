# Problem:
# Reference: https://www.acmicpc.net/problem/13549

# My Solution:
import sys
from collections import deque, defaultdict


def bfs(start, dest):
    q = deque([(start, 0)])
    visited = defaultdict(bool)
    while q:
        pos, cost = q.popleft()
        if pos == dest:
            print(cost)
            break
        if visited[pos]:
            continue
        visited[pos] = True
        if pos * 2 <= 100000:
            q.append((pos * 2, cost))
        if pos - 1 >= 0:
            q.append((pos - 1, cost + 1))
        if pos + 1 <= 100000:
            q.append((pos + 1, cost + 1))


N, K = map(int, sys.stdin.readline().split())
bfs(N, K)
