# Problem:
# Given a list of clothes; (name, category), return the number of combinations of clothes.
# Condition(s):
# 1. Only one item can be used in same category.

# My Solution:
import collections


def solution(clothes):
    answer = 0
    temp = []
    for i in clothes:
        temp.append(i[1])
    temp = collections.Counter(temp)
    answer = temp.values()
    mul = 1
    for i in answer:
        mul = mul * (i + 1)
    answer = mul - 1
    return answer
