# Problem:
# Reference: https://www.acmicpc.net/problem/11403

# My Solution:
import sys
from collections import deque


def bfs(s):
    q = deque([s])
    visited = set()
    answer = [0 for _ in range(N)]

    while q:
        pop = q.popleft()

        for c in conn[pop]:
            if s == c:
                answer[c] = 1
            if c not in visited:
                q.append(c)
                visited.add(c)
                answer[c] = 1

    return answer


N = int(sys.stdin.readline().rstrip())
conn = [[] for _ in range(N)]
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(len(temp)):
        if temp[j] == 1:
            conn[i].append(j)

for i in range(N):
    print(*bfs(i))
