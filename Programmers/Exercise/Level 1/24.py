# Problem:
# In Collatz conjecture, return the number of repetitions.
# Condition(s):
# 1. Return -1 if the repetitions exceed 500.

# My Solution:
def solution(num):
    cnt = 0
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        cnt += 1
        if cnt == 500:
            return -1
    return cnt
