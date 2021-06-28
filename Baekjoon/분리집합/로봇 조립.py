# Problem:
# Reference: https://www.acmicpc.net/problem/18116

# My Solution:
import sys
from collections import defaultdict

sys.setrecursionlimit(1000000000)


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
        cnt[tb] += cnt[ta]
        cnt[ta] = 0
    elif ta < tb:
        parent[tb] = ta
        cnt[ta] += cnt[tb]
        cnt[tb] = 0


N = int(sys.stdin.readline().rstrip())
parent = defaultdict(int)
cnt = defaultdict(int)
for i in range(1000001):
    parent[i] = i
    cnt[i] = 1

for _ in range(N):
    temp = sys.stdin.readline().split()
    if temp[0] == 'I':
        t1, t2 = int(temp[1]), int(temp[2])
        union(t1, t2)
    elif temp[0] == 'Q':
        t1 = int(temp[1])
        print(cnt[find(t1)])
