# Problem:
# Given a score board, return the maximum score when it goes down to the last row.
# Condition(s):
# 1. The score of the same column with the previous row cannot be obtained.

# My Solution:
def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            maximum = 0
            for k in range(4):
                if k == j:
                    continue
                if land[i][j] + land[i - 1][k] > maximum:
                    maximum = land[i][j] + land[i - 1][k]
            land[i][j] = maximum

    return max(land[-1])
