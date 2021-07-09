# Problem:
# Given a integer list, print the minimum and maximum number.

# My Solution:
import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    N = int(sys.stdin.readline().rstrip())
    nums = list(map(int, sys.stdin.readline().split()))
    print(min(nums), max(nums))
