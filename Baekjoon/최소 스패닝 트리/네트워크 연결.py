# Problem:
#

# My Solution:
import sys


def union(a, b):
    ta = find(a)
    tb = find(b)
    if ta < tb:
        parents[tb] = parents[ta]
    else:
        parents[ta] = parents[tb]


def find(target):
    if target == parents[target]:
        return target
    parents[target] = find(parents[target])
    return parents[target]


N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
parents = [i for i in range(N + 1)]

tot = 0
for cost in sorted(costs, key=lambda x: x[2]):
    a, b, c = cost
    if find(a) != find(b):
        union(a, b)
        tot += c
print(tot)
