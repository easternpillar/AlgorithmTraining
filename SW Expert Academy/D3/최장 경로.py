# Problem:
# Given the information of connections between nodes, print the length of the longest route.

# My Solution:
from collections import deque


def bfs(node, connect):
    q = deque([i, [i]] for i in range(1, node + 1, 1))
    mlen = 0
    while q:
        cur, visited = q.popleft()
        mlen = max(mlen, len(visited))

        for n in connect[cur]:
            temp = visited[:]
            if n in visited:
                continue
            else:
                temp.append(n)
                q.append([n, temp])
    return mlen


answer = []
for i in range(int(input())):
    N, M = map(int, input().split())
    if M == 0:
        answer.append(1)
        continue
    else:
        conn = [[] for _ in range(N + 1)]
        for j in range(M):
            f, t = map(int, input().split())
            conn[f].append(t)
            conn[t].append(f)
        answer.append(bfs(N, conn))

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
