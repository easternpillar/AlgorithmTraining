# Problem:
# Given a number to make and the number of numbers, return the set that the product of the elements is maximum.
# Condition(s):
# 1. Return the set with ascending order.

# My Solution:
def solution(n, s):
    answer = []
    q, r = divmod(s, n)
    if q <= 0:
        answer.append(-1)
    else:
        for i in range(n):
            answer.append(q)
        idx = 0
        while r > 0:
            answer[idx] += 1
            idx += 1
            if idx > len(answer) - 1:
                idx = idx % len(answer)
            r -= 1
    return sorted(answer)
