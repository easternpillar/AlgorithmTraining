# Problem:
# Given a string, return True if it has same number of 'p' and 'y' else False.
# Condition:
# 1. It is case-insensitive.

# My Solution:
def solution(s):
    answer = True
    pnum = 0
    ynum = 0
    for c in s:
        if c == 'p' or c == 'P':
            pnum += 1
        elif c == 'y' or c == 'Y':
            ynum += 1

    if pnum != ynum:
        answer = False
    return answer
