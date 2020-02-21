# Problem:
# Given the number of outer tiles and inner tiles, return the size of carpet.
# Condition(s):
# 1. It is longer in width than in length.

# My Solution:
def solution(brown, red):
    answer = []
    red_possible = []
    for i in range(red, 0, -1):
        if i < red // i:
            break
        if red % i == 0:
            red_possible.extend([[i, red // i]])

    for possible in red_possible:
        print(possible)
        if brown == (possible[0] + possible[1]) * 2 + 4:
            answer = [possible[0] + 2, possible[1] + 2]
            return answer
