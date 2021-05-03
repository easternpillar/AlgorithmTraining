# Problem:
# Given a list of natural numbers and a range, print the sum of numbers in range.

# My Solution:
import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
for i in range(1, len(nums)):
    nums[i] += nums[i - 1]

for _ in range(M):
    f, t = map(int, sys.stdin.readline().split())
    f -= 2
    t -= 1
    if f < 0:
        print(nums[t])
    else:
        print(nums[t] - nums[f])
