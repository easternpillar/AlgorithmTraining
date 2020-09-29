# Problem:
# Given 2 teams and the natural numbers for each member, return the maximum victory points that the second team can score.
# Condition(s):
# 1. The victory points can be scored if the natural number is bigger than the opposite's.

# My Solution:
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()

    idx_a = 0
    idx_b = 0
    while True:
        if idx_b >= len(B):
            break
        if B[idx_b] > A[idx_a]:
            answer += 1
            idx_a += 1
            idx_b += 1
        else:
            idx_b += 1

    return answer
