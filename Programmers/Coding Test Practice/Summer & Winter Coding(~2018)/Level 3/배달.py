# Problem:
# Given the number of villages, information on the roads connecting each village, and the time available for food delivery, return the number of villages that can receive food orders.

# # My Solution: DENIED.
# from collections import deque
#
# def search(s, e):
#     q = deque([[0, 0]])
#     costs = []
#     global cost
#     global k
#
#     while q:
#         pop = q.popleft()
#         start = pop[0]
#         time = pop[1]
#
#         for i in range(len(cost[start])):
#             if cost[start][i] == -1 or time + cost[start][i] > k:
#                 continue
#             if i == e:
#                 return True
#             else:
#                 q.append([i, time + cost[start][i]])
#     return False
#
#
# def solution(N, road, K):
#     answer = 0
#     global cost
#     global k
#     k = K
#     cost = [[-1 for i in range(N)] for j in range(N)]
#
#     for r in road:
#         if r[0] == r[1]:
#             continue
#         if cost[r[0] - 1][r[1] - 1] != -1:
#             if cost[r[0] - 1][r[1] - 1] > r[2]:
#                 cost[r[0] - 1][r[1] - 1] = r[2]
#                 cost[r[1] - 1][r[0] - 1] = r[2]
#         else:
#             cost[r[0] - 1][r[1] - 1] = r[2]
#             cost[r[1] - 1][r[0] - 1] = r[2]
#
#     if sum(cost[0]) == -1 * N:
#         return 1
#     visitable = []
#     for i in range(1, N):
#         if search(0, i):
#             visitable.append(i)
#
#     return len(visitable) + 1

import math
from collections import deque


def bfs(start, maps, distance, K):
    queue = deque()
    queue.append(start)

    distance[start] = 0

    while queue:
        y = queue.popleft()
        for x in range(1, len(maps)):

            if maps[y][x] != 0:

                if distance[x] > distance[y] + maps[y][x] and distance[y] + maps[y][x] <= K:
                    distance[x] = distance[y] + maps[y][x]
                    queue.append(x)

    return len([i for i in distance if i <= K])


def solution(N, road, K):
    distance = [math.inf for _ in range(N + 1)]

    # 마을 그래프 그리기
    maps = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for frm, to, w in road:

        if maps[frm][to] == 0 and maps[to][frm] == 0:
            maps[frm][to], maps[to][frm] = w, w
        else:
            if w < maps[frm][to]:
                maps[frm][to], maps[to][frm] = w, w

    return bfs(1, maps, distance, K)