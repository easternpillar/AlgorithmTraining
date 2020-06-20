# Problem:
# Given a number, return the next bigger number that meets the conditions.
# Condition(s):
# 1. The next number should be bigger than the number.
# 2. The next number should have same number of 1 when it is converted into binary number.

# My Solution:
def solution(n):
    temp = list(bin(n))
    cnt = temp[2:].count('1')
    while True:
        n += 1
        temp = list(bin(n))
        if cnt == temp[2:].count('1'):
            return n
