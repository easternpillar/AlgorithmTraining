# Problem:
# Given weights, return the minimum integer that cannot be weighed.

# My Solution: DENIED.
# def solution(weight):
#     answer = 0
#     weight.sort(reverse=True)
#
#     while True:
#         answer += 1
#         idx = 0
#         temp = answer
#         for i in range(len(weight)):
#             if weight[i] > temp:
#                 idx += 1
#                 continue
#             else:
#                 temp -= weight[i]
#         if temp != 0:
#             return answer


def solution(weight):
    answer = 1
    weight.sort()

    for w in weight:

        if answer >= w:
            answer += w

    return answer

# Learned:
# 1. Sum of weights + 1 = the minimum weight that cannot be measured.
