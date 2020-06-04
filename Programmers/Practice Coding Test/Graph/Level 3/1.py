# Problem:
# Given edges of a graph, return the number of the farthest nodes.

# My Solution: Denied.
# from collections import deque
#
#
# def solution(n, edge):
#     answer = 0
#     adj = [[] for i in range(n)]
#     for e in edge:
#         adj[e[0] - 1].append(e[1] - 1)
#         adj[e[1] - 1].append(e[0] - 1)
#
#     q = deque([[0, 0]])
#     dist = [-1 for i in range(n)]
#     visited = []
#
#     while q:
#         pop = q.popleft()
#         if dist[pop[0]] == -1:
#             dist[pop[0]] = pop[1]
#         if pop[0] in visited:
#             continue
#         else:
#             visited.append(pop[0])
#             for i in range(len(adj[pop[0]])):
#                 if adj[pop[0]][i] not in visited:
#                     q.append([adj[pop[0]][i], pop[1] + 1])
#
#     answer = dist.count(max(dist))
#     return answer

from collections import deque


def bfs(v, visited, adj):
    count = 0
    q = deque([[v, count]])
    while q:
        value = q.popleft()
        v = value[0]
        count = value[1]
        if visited[v] == -1:
            visited[v] = count
            count += 1
            for e in adj[v]:
                q.append([e, count])


def solution(n, edge):
    answer = 0
    visited = [-1] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    for e in edge:
        x = e[0]
        y = e[1]
        adj[x].append(y)
        adj[y].append(x)
    bfs(1, visited, adj)
    for value in visited:
        if value == max(visited):
            answer += 1
    return answer
