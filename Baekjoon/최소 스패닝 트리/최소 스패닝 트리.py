# Problem:
# Given the information of vertexes and edges, print the weigh of the minimum spanning tree.

# My Solution:
import sys


def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    ta = find(a)
    tb = find(b)
    if ta > tb:
        parent[ta] = tb
    else:
        parent[tb] = ta


V, E = map(int, sys.stdin.readline().split())
edges = []
parent = [i for i in range(V + 1)]
for i in range(E):
    edges.append(tuple(map(int, sys.stdin.readline().split())))
edges.sort(key=lambda x: x[2])

total = 0
for v1, v2, m in edges:
    if find(v1) != find(v2):
        union(v1, v2)
        total += m

print(total)
