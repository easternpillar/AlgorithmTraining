# Problem:
# Reference: https://www.acmicpc.net/problem/1325

# My Solution:
from collections import deque


def dfs(startnode):
    global trust

    visited = [0 for _ in range(N + 1)]
    stack = deque()
    stack.append(startnode)
    visited[startnode] = 1
    hacking = 1
    while stack:
        cur_node = stack.pop()

        for node in trust[cur_node]:
            if not visited[node]:
                visited[node] = 1
                hacking += 1
                stack.append(node)

    return hacking


import sys

N, M = map(int, sys.stdin.readline().split())
trust = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    trust[b].append(a)

answer = []
maxi = -1
for i in range(1, N + 1):
    temp = dfs(i)

    if temp > maxi:
        answer = [i]
        maxi = temp
    elif temp == maxi:
        answer.append(i)

answer.sort()
print(*answer)
