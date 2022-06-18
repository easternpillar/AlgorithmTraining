# Problem:
# Reference: https://www.acmicpc.net/problem/1197

# My Solution:
import sys


def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    ta, tb = find(a), find(b)
    if ta != tb:
        parent[ta] = tb


V, E = map(int, sys.stdin.readline().split())
parent = [i for i in range(V + 1)]
edges = []
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    edges.append((C, A, B))

edges.sort()
answer = 0
for e in edges:
    c, t1, t2 = e[0], e[1], e[2]
    if find(t1) == find(t2):
        continue
    union(t1, t2)
    answer += c
print(answer)
