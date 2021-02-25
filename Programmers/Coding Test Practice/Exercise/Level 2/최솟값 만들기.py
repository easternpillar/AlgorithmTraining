# Problem:
# Given 2 lists of numbers, return the minimum sum of the multiplication of pairs of the numbers.

# My Solution:
def solution(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])
