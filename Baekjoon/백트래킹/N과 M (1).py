# Problem:
# Reference: https://www.acmicpc.net/problem/15649

# My Solution:
import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
for perm in permutations([i for i in range(1, N + 1)], M):
    for p in perm:
        print(p, end=" ")
    print()

# Other Solution:
# import sys
# from collections import deque
#
#
# def backtrack(nums, n, m):
#     q = deque([[n]])
#     answer = []
#     while q:
#         pop = q.popleft()
#         if len(pop) == m:
#             answer.append(pop)
#             continue
#         for num in nums:
#             if num in pop:
#                 continue
#             temp = pop[:]
#             temp.append(num)
#             q.append(temp)
#     return answer
#
#
# N, M = map(int, sys.stdin.readline().split())
# nums = [i for i in range(1, N + 1)]
# for n in nums:
#     for back in backtrack(nums, n, M):
#         for b in back:
#             print(b, end=" ")
#         print()

# Other Solution:
# def backtracking(arr):
#     global answer
#
#     if len(arr) == M:
#         answer.append(arr)
#         return
#
#     for i in range(1, N + 1):
#
#         if visited[i] != 1:
#             visited[i] = 1
#             temp = arr[:]
#             temp.append(i)
#             backtracking(temp)
#             visited[i] = 0
#
#
# N, M = map(int, input().split())
#
# visited = [0] * (N + 1)
#
# answer = []
# backtracking([])
#
# print(answer)
