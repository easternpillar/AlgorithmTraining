# Problem:
# Reference: https://www.acmicpc.net/problem/1717

# My Solution:
import sys


def find(target):
    if target == parents[target]:
        return target
    parents[target] = find(parents[target])
    return parents[target]


def union(a, b):
    ta = find(a)
    tb = find(b)
    if not ta == tb:
        parents[tb] = ta


def check(a, b):
    if find(a) == find(b):
        return True
    else:
        return False


n, m = map(int, sys.stdin.readline().split())
parents = [i for i in range(n + 1)]

for _ in range(m):
    c, a, b = map(int, sys.stdin.readline().split())

    if c:
        if check(a, b):
            print("YES")
        else:
            print("NO")
    else:
        union(a, b)
