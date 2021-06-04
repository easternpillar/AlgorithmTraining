# Problem:
# Reference: https://www.acmicpc.net/problem/10815

# My Solution:
import sys
import bisect

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

answer = []
M = int(sys.stdin.readline().rstrip())
for find in list(map(int, sys.stdin.readline().split())):
    a = bisect.bisect_right(nums, find)
    if nums[a - 1] == find:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)
