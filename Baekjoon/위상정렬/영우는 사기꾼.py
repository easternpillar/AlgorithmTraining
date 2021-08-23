# Problem:
# Reference: https://www.acmicpc.net/problem/14676

# My Solution:
import sys
from collections import deque

flag = True
N, M, K = map(int, sys.stdin.readline().split())
indegrees = [0 for _ in range(N + 1)]
indegrees[0] = -1
conn = [[] for _ in range(N + 1)]
build = [0 for _ in range(N + 1)]
buildable = [False for _ in range(N + 1)]
for _ in range(M):
    X, Y = map(int, sys.stdin.readline().split())
    conn[X].append(Y)
    indegrees[Y] += 1

q = deque()
for i in range(1, N + 1):
    if indegrees[i] == 0:
        q.append(i)
        buildable[i] = True

for _ in range(K):
    f, c = map(int, sys.stdin.readline().split())
    if f == 1:
        if buildable[c]:
            build[c] += 1
            if build[c] == 1:
                for con in conn[c]:
                    indegrees[con] -= 1
                    if indegrees[con] == 0:
                        buildable[con] = True
        else:
            flag = False
            break
    elif f == 2:
        if build[c]:
            build[c] -= 1
            if build[c] == 0:
                for con in conn[c]:
                    buildable[con] = False
                    indegrees[con] += 1
        else:
            flag = False
            break

if flag:
    print("King-God-Emperor")
else:
    print("Lier!")
