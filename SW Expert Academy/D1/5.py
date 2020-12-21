# Problem:
# Given N scores as input, print the median value.
# Condition(s):
# 1. Numbers are odd numbers between 1 and 199.

# My Solution:
N = int(input())

temp = sorted(list(map(int, list(input().split()))))
print(temp[len(temp) // 2])
