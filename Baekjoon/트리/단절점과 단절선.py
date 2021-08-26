# Problem:
# Reference: https://www.acmicpc.net/problem/14675

# My Solution:
import sys


def node(start):
    if len(conn[start]) >= 2:
        return True
    else:
        return False


def edge(start):
    return True


N = int(sys.stdin.readline().rstrip())
conn = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    f, t = map(int, sys.stdin.readline().split())
    conn[f].append(t)
    conn[t].append(f)

for _ in range(int(sys.stdin.readline().rstrip())):
    t, k = map(int, sys.stdin.readline().split())
    if t == 1:
        if node(k):
            print('yes')
        else:
            print('no')
    elif t == 2:
        if edge(k):
            print('yes')
        else:
            print('no')
