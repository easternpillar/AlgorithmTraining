# Problem:
# Reference: https://www.acmicpc.net/problem/1717

# My Solution:
import sys

sys.setrecursionlimit(10 ** 9)


def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    ta, tb = find(a), find(b)
    if ta != tb:
        parent[ta] = tb


n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n + 1)]
for _ in range(m):
    c, a, b = map(int, sys.stdin.readline().split())
    if c == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
