# Problem:
# Reference: https://www.acmicpc.net/problem/1976

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


N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
conn = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
seq = list(map(int, sys.stdin.readline().split()))
parents = [i for i in range(N + 1)]

for i in range(len(conn)):
    for j in range(len(conn[i])):
        if conn[i][j] == 1:
            union(i, j)

flag = True
for i in range(len(seq)-1):
    if not check(seq[i]-1, seq[i + 1]-1):
        flag = False

if flag:
    print("YES")
else:
    print("NO")
