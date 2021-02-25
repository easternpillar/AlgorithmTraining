# Problem:
# Given a list of local budgets and total of having, return the total possible upper limit.
# Condition(s):
# 1. Same amount should be given to each region.

# My Solution:
def solution(budgets, M):
    answer = 0
    length = len(budgets)
    idx = 0
    budgets.sort()

    while True:
        q = M // (length - idx)

        if budgets[idx] >= q:
            return q
        else:
            while budgets[idx] <= q:
                M -= budgets[idx]
                idx += 1

                if idx >= length:
                    return budgets[idx - 1]

    return answer
