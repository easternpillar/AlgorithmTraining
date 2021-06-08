# Problem:
# Reference: https://www.acmicpc.net/problem/1647

# My Solution:
import sys


def find(target):
    if parent[target] == target:
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


N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N + 1)]
edges = []
nums = [0 for _ in range(N + 1)]
maxi = [0 for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    edges.append((C, A, B))

tot = 0
edges.sort(key=lambda x: x[0])
for e in edges:
    if find(e[1]) != find(e[2]):
        union(e[1], e[2])
        nums[e[1]] += 1
        nums[e[2]] += 1
        maxi[e[1]] = max(maxi[e[1]], e[0])
        maxi[e[2]] = max(maxi[e[2]], e[0])
        tot += e[0]

minus = 0
for i in range(N + 1):
    if nums[i] > 1 and maxi[i] > minus:
        minus = maxi[i]

print(tot - minus)
