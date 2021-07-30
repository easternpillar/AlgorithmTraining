# Problem:
# Reference: https://www.acmicpc.net/problem/15655

# My Solution:
import sys


def backtrack(start, li):
    li.append(nums[start])
    if len(li) == M:
        print(*li)
        return
    for i in range(start + 1, N, 1):
        backtrack(i, li[:])


N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

for i in range(N):
    backtrack(i, [])
