# Problem:
# Given the number of points and calories for each ingredient, print the maximum number of points that can be obtained without exceeding the calorie limit.

# My Solution:
from itertools import combinations


def calculate(comb, limit):
    calories = 0
    score = 0
    for c in comb:
        score += c[0]
        calories += c[1]

        if calories > limit:
            return False

    return score


T = int(input())
for i in range(T):
    N, L = map(int, input().split())
    mat = []
    max = 0
    print('#{}'.format(i + 1), end=" ")
    for j in range(N):
        mat.append(tuple(map(int, input().split())))
    for k in range(len(mat)+1):
        for c in list(combinations(mat, k)):
            con = calculate(c, L)
            if con > max:
                max = con

    print(max)
