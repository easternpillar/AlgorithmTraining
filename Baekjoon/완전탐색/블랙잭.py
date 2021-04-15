# Problem:
# Given a positive integer array and a target number, print the sum of 3 integers closest to the target number.

# My Solution:
import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
near = 0
for comb in list(combinations(nums, 3)):
    summ = sum(comb)
    if summ > M:
        continue
    if M - summ < M - near:
        near = summ
print(near)
