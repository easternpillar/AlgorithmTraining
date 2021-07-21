# Problem:
# Reference: https://www.acmicpc.net/problem/4195

# My Solution:
import sys
from collections import defaultdict


def find(target, parent):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target], parent)
    return parent[target]


def union(a, b, parent, cnt):
    ta = find(a, parent)
    tb = find(b, parent)
    if ta != tb:
        parent[ta] = tb
        cnt[tb] += cnt[ta]
        cnt[ta] = 0
    print(cnt[tb])


for _ in range(int(sys.stdin.readline().rstrip())):
    parent = defaultdict(str)
    cnt = defaultdict(int)
    for __ in range(int(sys.stdin.readline().rstrip())):
        a, b = sys.stdin.readline().split()
        if a not in parent.keys() and b not in parent.keys():
            parent[a] = a
            parent[b] = b
            cnt[a] = 1
            cnt[b] = 1
        elif a not in parent.keys():
            parent[a] = a
            cnt[a] = 1
        elif b not in parent.keys():
            parent[b] = b
            cnt[b] = 1
        union(a, b, parent, cnt)
