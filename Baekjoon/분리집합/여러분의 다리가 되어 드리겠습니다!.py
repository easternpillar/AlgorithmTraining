# Problem:
# Reference: https://www.acmicpc.net/problem/17352

# My Solution:
import sys
sys.setrecursionlimit(10**9)

def find(target):
    if parent[target] == target:
        return parent[target]
    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    ta, tb = find(a), find(b)
    if ta != tb:
        parent[ta] = tb


N = int(sys.stdin.readline().rstrip())
parent = [i for i in range(N + 1)]
for _ in range(N - 2):
    f, t = map(int, sys.stdin.readline().split())
    if find(f) != find(t):
        union(f, t)

s = set()
answer=[]
for i in range(1, N + 1):
    temp=find(i)
    if temp not in s:
        s.add(temp)
        answer.append(temp)
print(*answer)