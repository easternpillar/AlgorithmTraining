# Problem:
# Given a triangle that is made with integers, return the maximum value among the paths from the top to the bottom.
# Condition(s):
# 1. The path is only for diagonal left or right.

# My Solution:
def solution(triangle):
    answer = 0

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j != 0 and j != len(triangle[i]) - 1:
                triangle[i][j] = max(triangle[i - 1][j - 1:j + 1]) + triangle[i][j]
            elif j == 0:
                triangle[i][j] = triangle[i - 1][0] + triangle[i][j]
            else:
                triangle[i][j] = triangle[i - 1][-1] + triangle[i][j]
    answer = max(triangle[len(triangle) - 1])

    return answer
