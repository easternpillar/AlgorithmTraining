# Problem:
# Given two dummies of cards that positive integers are written, return the maximum score.
# Condition(s):
# 1. Left dummy card can be discarded anytime and right can discarded when left one is discarded.
# 2. Right dummy card can be discarded and get score of its value only if it has smaller value than left one.
# 3. The game will be finished when there is no card to be drawn.

# My Solution:
def solution(left, right):
    dp = [[-1 for i in range(len(right) + 1)] for i in range(len(left) + 1)]
    dp[0][0] = 0
    answer = 0
    print(dp)
    for i in range(len(left)):
        for j in range(len(right)):
            if dp[i][j] == -1:
                continue
            if left[i] > right[j] and dp[i][j + 1] < dp[i][j] + right[j]:
                dp[i][j + 1] = dp[i][j] + right[j]
            if dp[i + 1][j + 1] < dp[i][j]:
                dp[i + 1][j + 1] = dp[i][j]
            if dp[i + 1][j] < dp[i][j]:
                dp[i + 1][j] = dp[i][j]
            print(dp)

    for i in range(len(left)):
        if dp[i][len(right)] > answer:
            answer = dp[i][len(right)]
        if dp[i][len(left)] > answer:
            answer = dp[i][len(left)]
    return answer
