# Problem:
# Reference: https://www.acmicpc.net/problem/7662

# My Solution: DENIED.
# import bisect
# from collections import deque
# import sys
#
# T = int(sys.stdin.readline().rstrip())
# for i in range(T):
#     q = deque([])
#     k = int(sys.stdin.readline().rstrip())
#     for j in range(k):
#         command, num = sys.stdin.readline().split()
#
#         if command == 'I':
#             num = int(num)
#             q.insert(bisect.bisect_left(q, num), num)
#         else:
#             if not q:
#                 continue
#
#             if num == '-1':
#                 q.popleft()
#             else:
#                 q.pop()
#
#     if q:
#         print(q[-1], q[0])
#     else:
#         print("EMPTY")

import heapq
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    minq, maxq = [], []
    visited = [False for _ in range(1000001)]
    for i in range(int(input())):
        alpha, num = input().split()
        if alpha == 'I':
            heapq.heappush(minq, (int(num), i))
            heapq.heappush(maxq, (-int(num), i))
            visited[i] = True
        elif num == '-1':
            while minq and not visited[minq[0][1]]:
                heapq.heappop(minq)
            if minq:
                visited[minq[0][1]] = False
                heapq.heappop(minq)
        else:
            while maxq and not visited[maxq[0][1]]:
                heapq.heappop(maxq)
            if maxq:
                visited[maxq[0][1]] = False
                heapq.heappop(maxq)

    while minq and not visited[minq[0][1]]: heapq.heappop(minq)
    while maxq and not visited[maxq[0][1]]: heapq.heappop(maxq)
    print(f'{-maxq[0][0]} {minq[0][0]}' if maxq and minq else 'EMPTY')
