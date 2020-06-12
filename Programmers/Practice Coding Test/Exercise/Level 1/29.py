# Problem:
# Given an integer x and natural number n, return a list of n numbers starting with x and increasing by x.

# My Solution:
def solution(x, n):
    answer = [x * i for i in range(1, n + 1)]
    return answer
