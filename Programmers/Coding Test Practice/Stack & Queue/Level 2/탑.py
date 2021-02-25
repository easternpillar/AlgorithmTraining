# Problem:
# Given the heights of each tower, return index of tower which receive the signal.
# Condition(s):
# 1. Signal will be sent from right tower to left tower.
# 2. Signal will be received only when receiver tower is higher.
# 3. Only one tower can receive the signal.

# My Solution
def solution(heights):
    length = len(heights)
    answer = [0 for i in range(length)]

    for i in range(length):
        temp = heights.pop()
        for j in range(length - i - 2, -1, -1):
            if heights[j] > temp:
                answer[i] = j + 1
                break
    answer.reverse()

    return answer
