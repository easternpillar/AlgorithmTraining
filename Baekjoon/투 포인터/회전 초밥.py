# Problem:
# Reference: https://www.acmicpc.net/problem/15961

# My Solution:
import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def answer(N, d, k, c):
    left = right = 0
    re = 0
    while left < N:
        while right - left < k:
            if sushi[right] in have.keys():
                have[sushi[right]] += 1
            else:
                have[sushi[right]] = 1
            right += 1
        temp = len(have)
        if c not in have.keys():
            temp += 1
        re = max(re, temp)
        have[sushi[left]] -= 1
        if have[sushi[left]] <= 0:
            have.pop(sushi[left])
        left += 1
    return re


N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
sushi.extend(sushi[:k])
have = defaultdict(int)
print(answer(N, d, k, c))

# Other Solution(s):
# import sys
#
#
# def input():
#     return sys.stdin.readline().rstrip()
#
#
# def answer(line, max_seq, coupon):
#     count = 0
#     for i in range(max_seq):
#         food_number = line[i]
#         if not eat[food_number]:
#             count += 1
#         eat[food_number] += 1
#
#     max_count = count
#     for i in range(1, n):
#         if max_count <= count:
#             if not eat[coupon]:
#                 max_count = count + 1
#             else:
#                 max_count = count
#
#         out = i - 1
#         eat[line[out]] -= 1
#         if not eat[line[out]]:
#             count -= 1
#
#         in_ = (i + max_seq - 1) % n
#         if not eat[line[in_]]:
#             count += 1
#         eat[line[in_]] += 1
#
#     return max_count
#
#
# n, f_kind, max_seq, coupon = map(int, input().split())
# line = [int(input()) for _ in range(n)]
# eat = [0 for _ in range(3000001)]
# print(answer(line, max_seq, coupon))