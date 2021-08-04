# Problem:
# Reference: https://www.acmicpc.net/problem/16398

# My Solution:
import sys
sys.setrecursionlimit(10**9)


def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    ta, tb = find(a), find(b)
    if ta != tb:
        parent[ta] = tb


N = int(sys.stdin.readline().rstrip())
edges = []
parent = [i for i in range(N + 1)]
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(i + 1, len(temp), 1):
        edges.append((temp[j], i, j))

edges.sort(key=lambda x: x[0])
answer = 0
for edge in edges:
    if find(edge[1]) == find(edge[2]):
        continue
    union(edge[1], edge[2])
    answer += edge[0]

print(answer)
