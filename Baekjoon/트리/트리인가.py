# Problem:
# Reference: https://www.acmicpc.net/problem/6416

# My Solution:
import sys
from collections import defaultdict, deque


def bfs(start):
    q = deque([start])
    visited = {}
    for key in nodes:
        visited[key] = False
    while q:
        pop = q.popleft()
        if visited[pop]:
            return False
        visited[pop] = True
        for con in conn[pop]:
            q.append(con)
    if False in visited.values():
        return False
    else:
        return True


case = 0
seq = []
while True:
    temp = list(map(int, sys.stdin.readline().split()))
    if len(temp) == 2 and temp[0] < 0 and temp[1] < 0:
        break
    else:
        seq.extend(temp)
        if len(seq) >= 2:
            if seq[-1] == 0 and seq[-2] == 0:
                case += 1
                seq = seq[:len(seq) - 2]

                if not seq:
                    print("Case", case, "is a tree.")
                    seq = []
                    continue

                nodes = set(seq)
                conn = defaultdict(list)
                indegree = defaultdict(int)
                for i in range(0, len(seq), 2):
                    conn[seq[i]].append(seq[i + 1])
                    if seq[i] not in indegree.keys():
                        indegree[seq[i]] = 0
                    if seq[i + 1] not in indegree.keys():
                        indegree[seq[i + 1]] = 0
                    indegree[seq[i + 1]] += 1

                root = []
                for key in indegree.keys():
                    if indegree[key] == 0:
                        root.append(key)

                if len(root) > 1 or len(root) == 0:
                    print("Case", case, "is not a tree.")
                else:
                    if bfs(root[0]):
                        print("Case", case, "is a tree.")
                    else:
                        print("Case", case, "is not a tree.")
                seq = []
