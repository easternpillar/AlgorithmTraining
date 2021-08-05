# Problem:
# Reference: https://www.acmicpc.net/problem/10775

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


G = int(sys.stdin.readline().rstrip())
P = int(sys.stdin.readline().rstrip())
parent = [i for i in range(G + 1)]
answer = 0
for _ in range(P):
    g = int(sys.stdin.readline().rstrip())
    destination = find(g)
    if destination < 1:
        break
    else:
        union(destination, destination - 1)
        answer += 1
print(answer)
