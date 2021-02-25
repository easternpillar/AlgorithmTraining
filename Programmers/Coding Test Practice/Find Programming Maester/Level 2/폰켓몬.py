# Problem:
# Given a list of number, return the maximum number of distinct numbers.
# Condition(s):
# 1. The half amount of the list can be taken.

# My Solution:
def solution(nums):
    n = len(nums) // 2

    nums = set(nums)

    if len(nums) > n:
        return n
    else:
        return len(nums)
