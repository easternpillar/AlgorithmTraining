# Problem:
#

# My Solution:
import sys
from collections import deque

answer = [1]
n = int(sys.stdin.readline().rstrip())
conn = [[] for _ in range(n + 1)]
p = int(sys.stdin.readline().rstrip())

for i in range(p):
    a, b = map(int, sys.stdin.readline().split())
    conn[a].append(b)
    conn[b].append(a)

q = deque([1])
visited = []
while q:
    pop = q.popleft()
    if pop in visited:
        continue
    visited.append(pop)
    for node in conn[pop]:
        q.append(node)
        if node not in answer:
            answer.append(node)

print(len(answer) - 1)
