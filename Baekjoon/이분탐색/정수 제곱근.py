# Problem:
# Given a number, print the square root of the number.
# Condition(s):
# 1. The square root of the square must be greater than the original number.

# My Solution:
import math
import sys

n = int(sys.stdin.readline().rstrip())
sqrt = int(math.sqrt(n))
if sqrt ** 2 < n:
    sqrt += 1
print(int(sqrt))
