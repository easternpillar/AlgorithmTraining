# Problem:
# Reference: https://www.acmicpc.net/problem/18116

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
        parts[tb] += parts[ta]
        parts[ta] = 0


N = int(sys.stdin.readline().rstrip())
parent = [i for i in range(1000001)]
parts = [1 for i in range(1000001)]
for _ in range(N):
    temp = sys.stdin.readline().split()
    if temp[0] == 'I':
        union(int(temp[1]), int(temp[2]))
    else:
        print(parts[find(int(temp[1]))])
