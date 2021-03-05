# Problem:
# Given a list of Scoville degrees and minimum value K, return how many times should be mixed to satisfy the minimum value K.
# Condition(s):
# 1. Add first minimum and two times of second minimum.
# 2. Return -1 if it is impossible to make all values over K.

# My Solution: DENIED
# def solution(scoville, K):
#     answer = 0
#     scoville.sort(reverse=True)
#
#     while True:
#         first = scoville.pop()
#         if first >= K:
#             return answer
#         elif len(scoville) == 0:
#             return -1
#         second = scoville.pop()
#         answer = answer + 1
#         scoville.append(first + 2 * second)
#         scoville.sort(reverse=True)


from heapq import heapify, heappop, heappush


def solution(scoville, K):
    heapify(scoville)
    answer = 0
    while True:
        first = heappop(scoville)
        if first >= K:
            return answer
        elif len(scoville) == 0:
            return - 1
        second = heappop(scoville)
        answer = answer + 1
        heappush(scoville, first + second * 2)

