# Problem:
# Reference: https://www.acmicpc.net/problem/15656

# My Solution:
import sys

sys.setrecursionlimit(10 ** 9)


def backtrack(arr):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(N):
        temp = arr[:]
        temp.append(nums[i])
        backtrack(temp)


N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

for i in range(N):
    backtrack([nums[i]])
