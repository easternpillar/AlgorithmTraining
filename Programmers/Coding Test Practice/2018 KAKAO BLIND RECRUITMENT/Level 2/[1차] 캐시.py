# Problem:
# Given the cache size and a case of database requests, return the processing time.
# Condition(s):
# 1. 1 taken if cache hit.
# 2. 5 taken if cache miss.

# My Solution:
from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    for i in range(len(cities)):
        cities[i] = cities[i].lower()

    q = deque(cities)
    while q:
        pop = q.popleft()
        if pop in cache:
            answer += 1
            cache.remove(pop)
            cache.append(pop)
        else:
            cache.append(pop)
            if len(cache) > cacheSize:
                cache.popleft()
            answer += 5

    return answer
