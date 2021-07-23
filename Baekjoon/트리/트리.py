# Problem:
# Reference: https://www.acmicpc.net/problem/1068

# My Solution:
import sys
from collections import deque, defaultdict


def bfs1(start):
    q = deque([start])
    while q:
        pop = q.popleft()
        alive[pop] = False

        for con in conn[pop]:
            q.append(con)


def bfs2(start):
    q = deque([start])

    answer = 0
    while q:
        pop = q.popleft()
        flag = True
        if not alive[pop]:
            continue
        if conn[pop]:
            for con in conn[pop]:
                if alive[con]:
                    flag = False
                    q.append(con)
            if flag:
                answer += 1
        else:
            answer += 1
    return answer


N = int(sys.stdin.readline().rstrip())
alive = defaultdict(bool)
for i in range(N):
    alive[i] = True
conn = [[] for _ in range(N)]
parent = list(map(int, sys.stdin.readline().split()))
roots = set()
for i in range(len(parent)):
    if parent[i] == -1:
        roots.add(i)
        continue
    conn[parent[i]].append(i)

remove = int(sys.stdin.readline().rstrip())
bfs1(remove)
tot = 0
for root in roots:
    tot += bfs2(root)

print(tot)
