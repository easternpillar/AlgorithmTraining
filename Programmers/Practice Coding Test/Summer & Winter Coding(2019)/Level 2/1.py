# Problem:
# Given the lengths of the horizontal and vertical, return the number of squares available.
# Condition(s):
# 1. The square in the direction connecting the two diagonal vertices can not be used.

# My Solution:
import math


def solution(w, h):
    return w * h - (w + h - math.gcd(w, h))
