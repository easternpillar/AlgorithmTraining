# Problem:
# Given stock, dates and supplies, and deadline k, return how many times of minimum supplies should be taken by k day.
# Condition(s):
# 1. Start day is 0.
# 2. dates is sorted ascending order.

import heapq

# My Solution:
def solution(stock, dates, supplies, k):
    answer = 0
    idx = 0
    h = []
    while stock < k:
        for i in range(idx, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(h, (-supplies[i], supplies[i]))
                idx = i + 1
            else:
                break
        stock += heapq.heappop(h)[1]
        answer += 1
    return answer

# Learned:
# 1. Heap Queue reverse sorted: give priorities with (-) values and use values of index 1 of tuple.