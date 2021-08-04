# Problem:
# Reference: https://www.acmicpc.net/problem/10775

# My Solution: DENIED.
# import sys
# from collections import defaultdict
#
#
# def solution(P, isEmpty, answer):
#     for _ in range(P):
#         g = int(sys.stdin.readline().rstrip())
#         while isEmpty[g]:
#             g -= 1
#             if g == 0:
#                 return answer
#         isEmpty[g] = True
#         answer += 1
#     return answer
#
#
# G = int(sys.stdin.readline().rstrip())
# P = int(sys.stdin.readline().rstrip())
# isEmpty = defaultdict(bool)
# answer = 0
# print(solution(P, isEmpty, answer))

import sys


def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    ta = find(a)
    tb = find(b)
    if ta != tb:
        parent[ta] = tb


def solution():
    answer = 0
    for i in range(P):
        g = int(sys.stdin.readline().rstrip())
        dest = find(g)
        if dest < 1:
            break
        else:
            answer += 1
            union(dest, dest - 1)
    return answer


G = int(sys.stdin.readline().rstrip())
P = int(sys.stdin.readline().rstrip())
parent = [i for i in range(G+1)]
print(solution())
