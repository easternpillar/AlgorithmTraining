# Problem:
# Given mxn size routes and puddles, return the number of the shortest paths from (1,1) to (m,n).
# Condition(s):
# 1. Return the remainder value divided by 1,000,000,007.

# My Solution:
def solution(m, n, puddles):
    answer = 0
    matrix = [[1 for i in range(m)] for j in range(n)]

    for puddle in puddles:
        matrix[puddle[1] - 1][puddle[0] - 1] = 0
        if puddle[0] == 1:
            for i in range(puddle[1] - 1, n):
                matrix[i][0] = 0
        elif puddle[1] == 1:
            for i in range(puddle[0] - 1, m):
                matrix[0][i] = 0

    for i in range(1, n):
        for j in range(1, m):
            if [j + 1, i + 1] in puddles:
                continue
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

    answer = matrix[n - 1][m - 1]
    return answer % 1000000007