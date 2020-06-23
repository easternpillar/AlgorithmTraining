# Problem:
# Given the destination number, return the minimum battery capacity.
# Condition(s):
# 1. The jump can move one space with 1 battery consumption.
# 2. The teleport can move twice as long without using batteries.

# My Solution:
def solution(n):
    ans = 0
    while n != 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n -= 1
            ans += 1

    return ans
