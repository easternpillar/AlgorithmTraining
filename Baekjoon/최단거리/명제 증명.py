# Problem:
#

# My Solution:
import sys
from collections import defaultdict
from collections import deque


def bfs(start):
    visited = set()
    re = []
    q = deque(start)
    while q:
        pop = q.popleft()

        if pop in visited:
            continue

        visited.add(pop)

        for v in d[pop]:
            if v not in visited:
                q.append(v)

    for v in sorted(list(visited)):
        if v == start:
            continue
        re.append((start, v))

    return re


answer = []
N = int(sys.stdin.readline().rstrip())
d = defaultdict(list)
for _ in range(N):
    f, t = sys.stdin.readline().rstrip().split(' => ')
    d[f].append(t)

for key in list(d.keys()):
    answer.extend(bfs(key))

answer.sort(key=lambda x: (x[0], x[1]))
print(len(answer))
for a in answer:
    print(a[0], "=>", a[1])
